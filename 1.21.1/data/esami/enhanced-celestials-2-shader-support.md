# Enhanced Celestials 2: Shader Support (enhanced-celestials-2-shader-support)

File generato da `scripts/esamina.py` (workflow "Esamina mod"): la mod **non** è nel pack. Non modificarlo a mano.

- Versione: **2.0.0.3-neoforge** (release, 2026-09-03), file `Enhanced-Celestials-2-Shaders-NeoForge-1.21.1-2.0.0.3.jar`, id versione `4uOjogNm`
- Licenza su Modrinth: LicenseRef-All-Rights-Reserved · download: 51029
- Filtro dei valori: `-` · filtro dei testi del codice: `(?i)iris|uniform|shader|moon|sky|fog|colou?r`

## Mod nel file e dipendenze dichiarate

- `enhancedcelestials2shaders` 2.0.0.3
  - required: `neoforge` [21,)
  - required: `minecraft` [1.21.1,)
  - required: `enhancedcelestials2core` [2.0.3.1,)
  - required: `corgilib` [5.0.0.9,)
  - required: `sodium` *
  - required: `iris` *
  - incompatible: `enhancedcelestials` *

## Cartelle di dati (file .json)

- nessuna

## Testi nel codice


### `dev/corgitaco/enhancedcelestials2shaders/EnhancedCelestials2Shaders.class`

- "dev/corgitaco/enhancedcelestials2shaders/EnhancedCelestials2Shaders"
- "enhancedcelestials2shaders"
- "Ldev/corgitaco/enhancedcelestials2shaders/EnhancedCelestials2Shaders;"
- "EnhancedCelestials2Shaders.java"

### `dev/corgitaco/enhancedcelestials2shaders/LunarShadersMod.class`

- "dev/corgitaco/enhancedcelestials2shaders/LunarShadersMod"
- "LunarShadersMod already initialized!"
- "dev/corgitaco/enhancedcelestials2shaders/api/LunarEventUtils"
- "Ldev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper;"
- "Enhanced Celestials Shader Support"
- "dev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper"
- "enhancedcelestials2shaders"
- "Ldev/corgitaco/enhancedcelestials2shaders/LunarShadersMod;"
- "(Ldev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper;)V"
- "()Ldev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper;"
- "LunarShadersMod.java"

### `dev/corgitaco/enhancedcelestials2shaders/api/LunarEventUtils.class`

- "dev/corgitaco/enhancedcelestials2shaders/api/LunarEventUtils"
- "DEFAULT_COLOR_INTERNAL"
- "LunarShaders"
- "Ldev/corgitaco/enhancedcelestials2shaders/api/LunarEventUtils;"
- "getDefaultColor"
- "clampColor"
- "[LunarShaders] \u0001"

### `dev/corgitaco/enhancedcelestials2shaders/client/ClientLunarHandler.class`

- "dev/corgitaco/enhancedcelestials2shaders/client/ClientLunarHandler"
- "Ldev/corgitaco/enhancedcelestials2shaders/client/ClientLunarHandler;"
- "dev/corgitaco/enhancedcelestials2shaders/LunarShadersMod"
- "()Ldev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper;"
- "dev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper"
- "(Ldev/corgitaco/enhancedcelestials2shaders/client/ClientLunarHandler;)Ljava/util/function/Consumer;"
- "dev/corgitaco/enhancedcelestials2shaders/api/LunarEventUtils"
- "dev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer"
- "()Ldev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer;"
- "=== Lunar Shaders Client Debug ===\n"
- "()Ldev/corgitaco/enhancedcelestials2shaders/client/ClientLunarHandler;"

### `dev/corgitaco/enhancedcelestials2shaders/neoforge/EnhancedCelestialsShadersNeoForge.class`

- "dev/corgitaco/enhancedcelestials2shaders/EnhancedCelestials2Shaders"
- "enhancedcelestials2shaders"
- "dev/corgitaco/enhancedcelestials2shaders/neoforge/EnhancedCelestialsShadersNeoForge"
- "Ldev/corgitaco/enhancedcelestials2shaders/neoforge/EnhancedCelestialsShadersNeoForge;"
- "EnhancedCelestialsShadersNeoForge.java"

### `dev/corgitaco/enhancedcelestials2shaders/neoforge/LunarShadersNeoForge.class`

- "(Ldev/corgitaco/enhancedcelestials2shaders/neoforge/LunarShadersNeoForge;)Ljava/util/function/Consumer;"
- "dev/corgitaco/enhancedcelestials2shaders/neoforge/NeoForgeClientHandler"
- "dev/corgitaco/enhancedcelestials2shaders/neoforge/platform/NeoForgePlatformHelper"
- "dev/corgitaco/enhancedcelestials2shaders/LunarShadersMod"
- "(Ldev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper;)V"
- "dev/corgitaco/enhancedcelestials2shaders/neoforge/LunarShadersNeoForge"
- "Ldev/corgitaco/enhancedcelestials2shaders/neoforge/LunarShadersNeoForge;"
- "LunarShadersNeoForge.java"
- "enhancedcelestials2shaders"

### `dev/corgitaco/enhancedcelestials2shaders/neoforge/NeoForgeClientHandler.class`

- "dev/corgitaco/enhancedcelestials2shaders/neoforge/NeoForgeClientHandler"
- "dev/corgitaco/enhancedcelestials2shaders/client/ClientLunarHandler"
- "()Ldev/corgitaco/enhancedcelestials2shaders/client/ClientLunarHandler;"
- "dev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer"
- "()Ldev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer;"
- "getSkyColor"
- "getGlowColor"
- "renderColorGrading"
- "dev/corgitaco/enhancedcelestials2shaders/render/LunarEffectCompute"
- "DST_COLOR"
- "setShader"
- "POSITION_COLOR"
- "setColor"
- "drawWithShader"
- "Ldev/corgitaco/enhancedcelestials2shaders/neoforge/NeoForgeClientHandler;"
- "Ldev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer;"
- "color"
- "glowColor"
- "getPositionColorShader"
- "()Lnet/minecraft/client/renderer/ShaderInstance;"

### `dev/corgitaco/enhancedcelestials2shaders/neoforge/platform/NeoForgePlatformHelper.class`

- "dev/corgitaco/enhancedcelestials2shaders/neoforge/platform/NeoForgePlatformHelper"
- "iris"
- "net/irisshaders/iris/api/v0/IrisApi"
- "()Lnet/irisshaders/iris/api/v0/IrisApi;"
- "isShaderPackInUse"
- "dev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper"
- "Ldev/corgitaco/enhancedcelestials2shaders/neoforge/platform/NeoForgePlatformHelper;"
- "areShadersActive"

### `dev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper.class`

- "dev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper"
- "Ldev/corgitaco/enhancedcelestials2shaders/platform/PlatformHelper;"
- "areShadersActive"

### `dev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer.class`

- "dev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer"
- "Ldev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer;"
- "skyColor"
- "moonColor"
- "glowColor"
- "dev/corgitaco/enhancedcelestials2shaders/api/LunarEventUtils"
- "getSkyLightColor"
- "getMoonTextureColor"
- "resolveGlowColor"
- "getGlowColor"
- "Blend: %.2f | Active: %b | Sky: [%.2f, %.2f, %.2f]"
- "()Ldev/corgitaco/enhancedcelestials2shaders/render/LunarColorRenderer;"
- "lastSky"
- "currentSky"
- "lastMoon"
- "currentMoon"
- "getSkyColor"
- "getMoonColor"
- "sky"
- "lambda$resolveGlowColor$0"
- "LunarColorRenderer.java"

### `dev/corgitaco/enhancedcelestials2shaders/render/LunarEffectCompute.class`

- "dev/corgitaco/enhancedcelestials2shaders/render/LunarEffectCompute"
- "Ldev/corgitaco/enhancedcelestials2shaders/render/LunarEffectCompute;"
- "colorBlend"
