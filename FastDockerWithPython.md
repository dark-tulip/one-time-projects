💾 Шаг 1: Структура проекта
```
my_service/
├── app/
│   ├── main.py
│   ├── requirements.txt
├── docker-compose.yml
├── Dockerfile
```
📜 app/main.py — простой сервис Python
```python

import psycopg2
import os

# тут подключаемся к БД из докер контейнера
def connect_and_fetch():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),  # берем hostname, (не по localhost, a по имени хоста)
        database=os.getenv("POSTGRES_DB", "testdb"),
        user=os.getenv("POSTGRES_USER", "user"),
        password=os.getenv("POSTGRES_PASSWORD", "password")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books;") # прочитать книжки
    rows = cursor.fetchall()

    for row in rows:
        print(row) # напечатать их

    cursor.close()
    conn.close()

if __name__ == "__main__":
    connect_and_fetch()

```

📦 app/requirements.txt
```
psycopg2-binary
```

🐳 Dockerfile

```Dockerfile
Копировать
Редактировать
FROM python:3.11-slim

WORKDIR /app
COPY app/ /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
```

🐙 docker-compose.yml

```yaml
version: '3.9'

services:
  postgres:
    image: postgres:14
    environment:
      POSTGRES_DB: testdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql  # создаем несколько тестовых БД c пользователями
    ports:
      - "5432:5432"

  python_app:
    build: .  # Взять докерфайл и создать образ
    depends_on:
      - db    # сначала должна подняться БД
    environment:  # тут передаем параметры для подключения к БД приложению на питоне
      DB_HOST: postgres    ## hostname внутри сети докера
      POSTGRES_DB: testdb  ## название БД
      POSTGRES_USER: user  ## юзер для подключения к БД
      POSTGRES_PASSWORD: password

volumes:
  pgdata:
```

📌 init.sql
- этот скрипт запустится, только один раз, когда мы впервые поднимем контейнер

```sql
-- Создание таблицы и вставка данных
CREATE TABLE books
(
    id             BIGSERIAL PRIMARY KEY,
    title          text NOT NULL,
    author         text NOT NULL,
    published_year INTEGER
);

INSERT INTO books (title, author, published_year)
VALUES ('1984', 'George Orwell', 1949),
       ('To Kill a Mockingbird', 'Harper Lee', 1960),
       ('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
       ('Pride and Prejudice', 'Jane Austen', 1813),
       ('The Catcher in the Rye', 'J.D. Salinger', 1951);
```
