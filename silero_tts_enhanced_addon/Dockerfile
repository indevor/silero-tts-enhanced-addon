FROM python:3.11-slim

WORKDIR /app

# Добавили libsndfile1 (критически важно для сохранения аудио нейросетями)
RUN apt-get update && apt-get install -y gcc libsndfile1 ffmpeg \
    && pip install --no-cache-dir fastapi uvicorn silero-tts==0.0.5 pydantic scipy \
    && rm -rf /var/lib/apt/lists/*

COPY main.py /app/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8014"]