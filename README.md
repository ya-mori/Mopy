# Mopy
Simple tool to create mock data

# 使い方

サンプルコード
```
users = Table(
    "users",
    id=PkIntSeed(),
    age=RandIntSeed(min=0, max=10),
    name=RandStrSeed(size=5),
    birth=RandDateSeed()
)

items = Table(
    "items",
    id=PkIntSeed(),
    price=RandIntSeed(min=0, max=100),
    user_id=users("id"),
    type=EnumSeed(["ONE", "TWO", "THERE"]),
    isActive=RandBoolSeed()
)

for query in users.create(10).to_sql():
    print(query)

for query in items.create(10).to_sql():
    print(query)
```

実行結果
```
INSERT INTO users(id, age, name, birth) VALUES (1, 8, tU0S1, 1945-04-28);
INSERT INTO users(id, age, name, birth) VALUES (2, 4, XM8oa, 2065-03-09);
INSERT INTO users(id, age, name, birth) VALUES (3, 5, sMNsV, 1981-01-07);
INSERT INTO users(id, age, name, birth) VALUES (4, 2, pciNm, 1943-02-27);
INSERT INTO users(id, age, name, birth) VALUES (5, 0, rURTE, 2032-09-29);
INSERT INTO users(id, age, name, birth) VALUES (6, 5, Sjpft, 1961-02-24);
INSERT INTO users(id, age, name, birth) VALUES (7, 8, k1xP1, 1946-03-05);
INSERT INTO users(id, age, name, birth) VALUES (8, 10, eahgp, 1959-09-08);
INSERT INTO users(id, age, name, birth) VALUES (9, 4, JM6tD, 2063-06-08);
INSERT INTO users(id, age, name, birth) VALUES (10, 1, O9uc6, 1959-09-07);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (1, 33, 1, TWO, True);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (2, 62, 2, TWO, False);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (3, 13, 3, TWO, False);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (4, 75, 4, TWO, False);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (5, 50, 5, TWO, False);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (6, 63, 6, THERE, False);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (7, 82, 7, THERE, False);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (8, 68, 8, THERE, True);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (9, 76, 9, TWO, False);
INSERT INTO items(id, price, user_id, type, isActive) VALUES (10, 33, 10, ONE, True);
```
