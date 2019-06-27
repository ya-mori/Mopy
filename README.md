# Mopy
Simple tool to create mock data

# 使い方

サンプルコード
``` sample.py
users = Table(
    "users",
    id=PkIntSeed(),
    age=RandIntSeed(min=0, max=100),
    name=RandStrSeed(size=5),
    birth=RandDateSeed()
)

items = Table(
    "items",
    id=PkIntSeed(),
    price=RandIntSeed(min=0, max=1000),
    user_id=users("id"),
    user_name=users("name"),
    type=EnumSeed(["ONE", "TWO", "THERE"]),
    is_active=RandBoolSeed()
)

users.create(7).show_sql()
items.create(5).show_sql()
```

実行結果
``` output.sql
INSERT INTO users(id, age, name, birth) VALUES (1, 53, 'a3X6w', 1953-07-03);
INSERT INTO users(id, age, name, birth) VALUES (2, 74, 'g2bqS', 2045-06-05);
INSERT INTO users(id, age, name, birth) VALUES (3, 32, '5KXmT', 1931-07-02);
INSERT INTO users(id, age, name, birth) VALUES (4, 75, 'YHbwC', 1938-01-14);
INSERT INTO users(id, age, name, birth) VALUES (5, 5, 'jHaTc', 2031-02-13);
INSERT INTO users(id, age, name, birth) VALUES (6, 14, 'CBPfh', 2087-09-26);
INSERT INTO users(id, age, name, birth) VALUES (7, 58, '47tJr', 1931-02-26);
INSERT INTO items(id, price, user_id, user_name, type, is_active) VALUES (1, 611, 1, 'a3X6w', 'THERE', False);
INSERT INTO items(id, price, user_id, user_name, type, is_active) VALUES (2, 790, 2, 'g2bqS', 'ONE', True);
INSERT INTO items(id, price, user_id, user_name, type, is_active) VALUES (3, 503, 3, '5KXmT', 'THERE', False);
INSERT INTO items(id, price, user_id, user_name, type, is_active) VALUES (4, 919, 4, 'YHbwC', 'TWO', False);
INSERT INTO items(id, price, user_id, user_name, type, is_active) VALUES (5, 451, 5, 'jHaTc', 'ONE', True);
```
