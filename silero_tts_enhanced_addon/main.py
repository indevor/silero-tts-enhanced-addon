import os
import tempfile
from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from silero_tts.silero_tts import SileroTTS

app = FastAPI()

tts_engine = None
current_model = None

class TTSRequest(BaseModel):
    text: str
    voice: str = "aidar"
    language: str = "ru"
    model_id: str = "v5_ru"
    sample_rate: int = 48000

@app.post("/tts")
def generate_tts(req: TTSRequest):
    global tts_engine, current_model
    try:
        # Инициализация модели
        if tts_engine is None or current_model != req.model_id:
            print(f"Загрузка модели: {req.model_id}")
            tts_engine = SileroTTS(model_id=req.model_id, language=req.language, speaker=req.voice)
            current_model = req.model_id
        
        # Смена языка и голоса
        if getattr(tts_engine, 'language', '') != req.language:
            tts_engine.change_language(req.language)
        if getattr(tts_engine, 'speaker', '') != req.voice:
            tts_engine.change_speaker(req.voice)
            
        # Установка частоты (официальный метод библиотеки)
        if hasattr(tts_engine, 'change_sample_rate'):
            tts_engine.change_sample_rate(req.sample_rate)

        # Подготовка файла
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            temp_path = tmp.name
            
        print(f"Генерация: текст='{req.text}', голос={req.voice}")
        tts_engine.tts(req.text, temp_path)
        
        # Проверка, что аудио реально создалось и оно не 0 байт
        if not os.path.exists(temp_path) or os.path.getsize(temp_path) == 0:
            raise Exception("Файл не сгенерировался (0 байт). Ошибка библиотеки Silero.")
            
        with open(temp_path, "rb") as f:
            audio = f.read()
            
        os.remove(temp_path)
        print(f"Успех! Отправлено {len(audio)} байт.")
        return Response(content=audio, media_type="audio/wav")

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))