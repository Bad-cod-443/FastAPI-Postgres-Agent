import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from dotenv import load_dotenv

# Подгружаем пароли из .env
load_dotenv()

app = FastAPI(title="Caine AI Memory API")

# Конфигурация через переменные окружения
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("Tap81rus!")
}

# Модель данных для записи
class MemoryItem(BaseModel):
    topic: str
    fact: str
    importance: int

@app.get("/memory")
def get_memory():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ai_memory ORDER BY importance DESC;")
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/memory/add")
def add_memory(item: MemoryItem):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO ai_memory (topic, fact, importance) VALUES (%s, %s, %s);"
        cursor.execute(query, (item.topic, item.fact, item.importance))
        conn.commit()
        cursor.close()
        conn.close()
        return {"status": "added", "item": item}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))