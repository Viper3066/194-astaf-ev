import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('european_database.sqlite')
cursor = conn.cursor()
# Получение списка всех таблиц
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Таблицы в базе данных:")
for table in tables:
    print(f"\nТаблица: {table[0]}")
    # Получение структуры таблицы
    cursor.execute(f"PRAGMA table_info({table[0]});")
    columns = cursor.fetchall()

    print("Структура таблицы:")
    for column in columns:
        print(f" - {column[1]} (Тип: {column[2]}, NULL: {column[3]}, Дефолт: {column[4]})")

    # Получение первых 5 записей из таблицы
    cursor.execute(f"SELECT * FROM {table[0]} LIMIT 5;")
    records = cursor.fetchall()

    print("Примеры записей:")
    for record in records:
        print(f" - {record}")
# Закрытие соединения
conn.close()