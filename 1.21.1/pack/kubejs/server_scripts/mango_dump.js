// Mango Craft — dump dei dati del gioco per la base dati del repository (dalla 0.7.2).
//
// Comando: /mango_dump   (giocatore in single player o operatore)
// Scrive in logs/mango-craft-dump/ dell'istanza (cartella dei log: la stessa che Claude legge già per le prove):
//   meta.json      data, versioni di Minecraft e KubeJS, mod caricate con la versione, errori di ogni sezione
//   effetti.json   ogni effetto: categoria del gioco (beneficial, harmful, neutral), istantaneo, colore
//   pozioni.json   ogni pozione: nome di traduzione ed effetti con durata (tick) e livello (0 = I)
//   alambicco.json le ricette dell'alambicco provate davvero (ingrediente × pozione → risultato), più le ricette
//                  NeoForge che il gioco elenca (anche quelle con un ingresso che non è una pozione)
//   oggetti.json   gli oggetti con effetti di serie: cibi e bevande (FoodProperties) e oggetti con pozione dentro
// I file li importa scripts/dump_importa.py nel repository (1.21.1/data/dump/); la base dati li legge da lì.
// Non cambia niente nel mondo: legge soltanto. Ogni sezione è protetta: se una fallisce, le altre si scrivono e
// l'errore finisce in meta.json.
//
// Nessun nome al primo livello dello script: KubeJS ci tiene i suoi (Items, Item, Text…) e un `const` con lo stesso
// nome blocca il caricamento ("redeclaration of var Items", prova del 25/10/2026). Tutto sta dentro il comando.

ServerEvents.basicCommand('mango_dump', event => {
  const DIR = 'logs/mango-craft-dump/'
  const $BuiltInRegistries = Java.loadClass('net.minecraft.core.registries.BuiltInRegistries')
  const $DataComponents = Java.loadClass('net.minecraft.core.component.DataComponents')
  const $ItemStack = Java.loadClass('net.minecraft.world.item.ItemStack')
  const $Items = Java.loadClass('net.minecraft.world.item.Items')
  const $PotionContents = Java.loadClass('net.minecraft.world.item.alchemy.PotionContents')
  const $Potion = Java.loadClass('net.minecraft.world.item.alchemy.Potion')
  const $Optional = Java.loadClass('java.util.Optional')

  const idOf = (registry, value) => {
    const key = registry.getKey(value)
    return key == null ? null : String(key)
  }
  const effectInstance = inst => {
    return {
      effetto: idOf($BuiltInRegistries.MOB_EFFECT, inst.getEffect().value()),
      durata: Number(inst.getDuration()),
      livello: Number(inst.getAmplifier())
    }
  }
  const potionOf = stack => {
    const pc = stack.get($DataComponents.POTION_CONTENTS)
    if (pc == null || !pc.potion().isPresent()) return null
    return idOf($BuiltInRegistries.POTION, pc.potion().get().value())
  }
  const stackInfo = stack => {
    const out = { oggetto: idOf($BuiltInRegistries.ITEM, stack.getItem()), quanti: Number(stack.getCount()) }
    const p = potionOf(stack)
    if (p != null) out.pozione = p
    return out
  }
  // un array Java (Ingredient.getItems()) non ha forEach: si scorre per indice
  const stacksOf = arr => {
    const out = []
    for (let i = 0; i < arr.length; i++) out.push(stackInfo(arr[i]))
    return out
  }

  const level = event.getLevel()
  const meta = {
    formato: 1,
    data: new Date().toISOString(),
    minecraft: String(Platform.getMinecraftVersionString()),
    kubejs: String(Platform.getModVersion()),
    mod: {},
    file: {},
    errori: []
  }
  const section = (name, fn) => {
    try {
      const data = fn()
      JsonIO.write(DIR + name + '.json', data)
      meta.file[name] = Array.isArray(data) ? data.length : data.miscele.length
    } catch (e) {
      meta.errori.push(name + ': ' + e)
    }
  }

  try {
    Platform.getMods().forEach((id, info) => { meta.mod[String(id)] = String(info.getVersion()) })
  } catch (e) {
    meta.errori.push('mod: ' + e)
  }

  section('effetti', () => {
    const out = []
    $BuiltInRegistries.MOB_EFFECT.keySet().forEach(rl => {
      const eff = $BuiltInRegistries.MOB_EFFECT.get(rl)
      out.push({
        id: String(rl),
        categoria: String(eff.getCategory()).toLowerCase(),
        istantaneo: !!eff.isInstantenous(),
        colore: Number(eff.getColor()),
        traduzione: String(eff.getDescriptionId())
      })
    })
    return out
  })

  section('pozioni', () => {
    const out = []
    $BuiltInRegistries.POTION.keySet().forEach(rl => {
      const potion = $BuiltInRegistries.POTION.get(rl)
      const holder = $BuiltInRegistries.POTION.wrapAsHolder(potion)
      const row = { id: String(rl), effetti: [] }
      try {
        row.traduzione = String($Potion.getName($Optional.of(holder), ''))
      } catch (e) {
        row.traduzione = null
      }
      potion.getEffects().forEach(inst => row.effetti.push(effectInstance(inst)))
      out.push(row)
    })
    return out
  })

  section('alambicco', () => {
    const brewing = level.potionBrewing()
    const ingredienti = []
    $BuiltInRegistries.ITEM.keySet().forEach(rl => {
      const s = $BuiltInRegistries.ITEM.get(rl).getDefaultInstance()
      try {
        if (brewing.isIngredient(s)) ingredienti.push(s)
      } catch (e) { /* una ricetta personalizzata può non accettare oggetti strani */ }
    })
    const contenitori = [$Items.POTION, $Items.SPLASH_POTION, $Items.LINGERING_POTION]
    const miscele = []
    $BuiltInRegistries.POTION.keySet().forEach(rl => {
      const holder = $BuiltInRegistries.POTION.wrapAsHolder($BuiltInRegistries.POTION.get(rl))
      contenitori.forEach(c => {
        const input = $PotionContents.createItemStack(c, holder)
        ingredienti.forEach(ing => {
          try {
            if (!brewing.hasMix(input, ing)) return
            const res = brewing.mix(ing, input.copy())
            if (res.isEmpty() || $ItemStack.isSameItemSameComponents(res, input)) return
            miscele.push({ ingresso: stackInfo(input), ingrediente: idOf($BuiltInRegistries.ITEM, ing.getItem()), risultato: stackInfo(res) })
          } catch (e) { /* idem */ }
        })
      })
    })
    const ricette = []
    brewing.getRecipes().forEach(r => {
      const row = { classe: String(r.getClass().getName()) }
      try {
        row.ingresso = stacksOf(r.getInput().getItems())
        row.ingrediente = stacksOf(r.getIngredient().getItems())
        row.risultato = stackInfo(r.getOutput())
      } catch (e) {
        delete row.ingresso
        delete row.ingrediente
        delete row.risultato
        row.nota = 'ricetta con logica propria: ingressi non elencabili'
      }
      ricette.push(row)
    })
    return { ingredienti: ingredienti.map(s => idOf($BuiltInRegistries.ITEM, s.getItem())), miscele: miscele, ricette: ricette }
  })

  section('oggetti', () => {
    const out = []
    const pozioni = ['minecraft:potion', 'minecraft:splash_potion', 'minecraft:lingering_potion', 'minecraft:tipped_arrow']
    $BuiltInRegistries.ITEM.keySet().forEach(rl => {
      const id = String(rl)
      const s = $BuiltInRegistries.ITEM.get(rl).getDefaultInstance()
      const row = { id: id }
      const food = s.get($DataComponents.FOOD)
      if (food != null) {
        row.cibo = {
          nutrizione: Number(food.nutrition()),
          saturazione: Number(food.saturation()),
          sempre: !!food.canAlwaysEat(),
          secondi: Number(food.eatSeconds()),
          effetti: []
        }
        food.effects().forEach(pe => {
          const r = effectInstance(pe.effectSupplier().get())
          r.probabilita = Number(pe.probability())
          row.cibo.effetti.push(r)
        })
      }
      const pc = s.get($DataComponents.POTION_CONTENTS)
      if (pc != null && pozioni.indexOf(id) < 0) {
        row.pozione = { id: pc.potion().isPresent() ? idOf($BuiltInRegistries.POTION, pc.potion().get().value()) : null, effetti: [] }
        pc.getAllEffects().forEach(inst => row.pozione.effetti.push(effectInstance(inst)))
      }
      if (row.cibo || row.pozione) out.push(row)
    })
    return out
  })

  JsonIO.write(DIR + 'meta.json', meta)
  event.respond(Text.of('Mango Craft: dump scritto in ' + DIR + ' (' + JSON.stringify(meta.file) + ', errori: ' + meta.errori.length + ')'))
})
