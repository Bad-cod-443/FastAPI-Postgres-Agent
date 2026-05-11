import psycopg2

db_config = {
    "host": "localhost",
    "port": "5432",
    "database": "postgres", 
    "user": "postgres",
    "password": "" 
}

try:

    print("Подключение к базе данных...")
    connection = psycopg2.connect(**db_config)
    
   
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM ai_memory ORDER BY importance DESC;")
    
    # Забираем все полученные строки
    memories = cursor.fetchall()
    
    # выводим результат в консоль
    print("\n Память агента Caine успешно загружена:")
    print("-" * 50)
    
    for row in memories:
        # row - это кортеж (tuple) со значениями колонок: (id, topic, fact, importance)
        print(f"[{row[3]}/10] {row[1].upper()}: {row[2]}")

except Exception as error:
    print("\n Ошибка при работе с PostgreSQL:", error)

finally:
   
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("-" * 50)
        print("Соединение с БД закрыто.")
