# Silero TTS Enhanced Engine

A local, fast, and high-quality text-to-speech synthesizer for your smart home.

This add-on is based on [Silero Models](https://github.com/snakers4/silero-models) neural network models and uses an improved text processing algorithm from [daswer123](https://github.com/daswer123/silero-tts-enhanced).

## 🔥 Features
* **Works locally:** No cloud or internet required.
* **Fast switching:** Models are stored in RAM.
* **Stress:** You can explicitly specify stress in complex words by placing a `+` sign before a vowel (e.g., `zam+ok`).

## 🛠 Available Models and Languages
The add-on automatically downloads any model you request from the Integration.
Most popular:
* **Russian (ru):** `v5_ru` (voices: aidar, baya, kseniya, xenia, random)
* **English (en):** `v3_en` (117 voices: en_0, en_1 ... en_117)

## 💡 Automation examples
You can change the voice and model on the fly directly from Home Assistant scripts:

```yaml
service: tts.speak
target:
  entity_id: tts.silero_tts_enhanced
data:
  media_player_entity_id: media_player.living_room
  message: “Attention. The CPU temperature has reached 80 degrees.”
  options:
    model_id: “v5_ru”
    voice: “xenia”
    put_accent: true

service: tts.speak
target:
  entity_id: tts.silero_tts_enhanced
data:
  media_player_entity_id: media_player.living_room
  message: “Hello world, the smart home is ready.”
  language: “en”
  options:
    model_id: “v3_en”
    voice: “en_24”
```

----------------------------------------------------------

# Silero TTS Enhanced Engine

Локальный, быстрый и качественный синтезатор речи для вашего Умного дома.

Этот аддон основан на нейросетевых моделях [Silero Models](https://github.com/snakers4/silero-models) и использует улучшенный алгоритм обработки текста от [daswer123's](https://github.com/daswer123/silero-tts-enhanced).

## 🔥 Возможности
* **Работает локально:** Без облаков и интернета.
* **Быстрое переключение:** Модели хранятся в ОЗУ.
* **Ударения:** Вы можете явно указать ударение в сложных словах, поставив знак `+` перед гласной (например: `зам+ок`).

## 🛠 Доступные модели и языки
Аддон автоматически скачивает любую модель, которую вы запросите из Интеграции.
Самые популярные:
* **Русский (ru):** `v5_ru` (голоса: aidar, baya, kseniya, xenia, random)
* **Английский (en):** `v3_en` (117 голосов: en_0, en_1 ... en_117)

## 💡 Примеры автоматизаций
Можено менять голос и модель прямо "на лету" из скриптов Home Assistant:

```yaml
service: tts.speak
target:
  entity_id: tts.silero_tts_enhanced
data:
  media_player_entity_id: media_player.living_room
  message: "Внимание. Температура процессора достигла 80 градусов."
  options:
    model_id: "v5_ru"
    voice: "xenia"
    put_accent: true

service: tts.speak
target:
  entity_id: tts.silero_tts_enhanced
data:
  media_player_entity_id: media_player.living_room
  message: "Hello world, the smart home is ready."
  language: "en"
  options:
    model_id: "v3_en"
    voice: "en_24"
```