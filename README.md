# Caine AI - Long-term Memory API

REST API сервис для управления долгосрочной памятью AI-агента. Построен на FastAPI и PostgreSQL. Позволяет агенту сохранять контекст, новые факты и извлекать их для формирования ответов (фундамент для RAG-архитектуры).

## Стек технологий
* **Backend:** Python 3, FastAPI, Uvicorn
* **Database:** PostgreSQL
* **Driver:** psycopg2-binary
* **Data Validation:** Pydantic

## Запуск проекта

1. Клонируйте репозиторий:
   git clone https://github.com/Bad-cod-443/FastAPI-Postgres-Agent.git
   
2. Установите зависимости:
   pip install -r requirements.txt
   
3. Создайте файл `.env` в корневой папке и добавьте настройки БД:
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=ваш_пароль
   
4. Запустите сервер:
   python -m uvicorn server:app --reload

## Документация API
После запуска сервера интерактивная документация (Swagger UI) доступна по адресу: `http://127.0.0.1:8000/docs`
