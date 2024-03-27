## Задание

Написать inner-join на MapReduce (ReduceSideJoin) для двух таблиц по полю `product_id`.

## Решение

Сначала реализуем 2 mapper'a для каждой из соединяемых таблиц, чтобы в исходные 
строки добавить переменную `table_type`.

Затем для финальной MapReduce-задачи используется простейший mapper, который не имеет 
в себе никакой логики и reducer, в котором происходит JOIN.

JOIN выполняется с использованием вложенных циклов (несколько похоже на Nested Loops Join).
Это можно легко реализовать, так как входные строки сортируются по первому ключу, которым является 
поле, по которому происходит JOIN.

## Пример

Выполним MapReduce (Map-only) с изначальными таблицами. Сначала считаем табличку с 
ценами и выведем ее с использованием table_type:

```
mapred streaming \
-D mapred.reduce.tasks=0 \
-input data/data1/shop_price.csv \
-output data/output1/mr3_price \
-mapper mr3_price_mapper.py \
-file hadoop1/script1/mr3_price_mapper.py
```

Результат Map-only-задачи для таблицы с ценами:

| product_id (key) | type   | price (value) |
|------------------|--------|---------------|
| 5                | price  | 35.32         |
| 7                | price  | 127.08        |
| 10               | price  | 114.78        |
| 1                | price  | 29.96         |
| 8                | price  | 84.82         |
| 2                | price  | 26.03         |
| 1                | price  | 15.43         |
| 7                | price  | 111.79        |
| 3                | price  | 31.87         |
| 6                | price  | 46.43         |

Затем считаем табличку с описаниями и выведем ее с использованием table_type:

```
mapred streaming \
-D mapred.reduce.tasks=0 \
-input data/data1/shop_product.csv \
-output data/output1/mr3_product \
-mapper mr3_product_mapper.py \
-file hadoop1/script1/mr3_product_mapper.py
```

Результат Map-only-задачи для таблицы с описаниями:

| product_id (key) | type   | description (value) |
|------------------|--------|----------------------|
| 3                | price  | Лук репчатый, кг     |
| 6                | price  | Морковь, кг          |
| 5                | price  | Свекла, кг           |
| 7                | price  | Яблоки, кг           |
| 8                | price  | Апельсины, кг        |
| 2                | price  | Капуста свежая, кг   |
| 1                | price  | Картофель, кг        |
| 9                | price  | Клубника, кг         |


Теперь, используя результаты прошлый MapReduce-задач, выполним последний MapReduce, где как раз
выполняется JOIN:

```
mapred streaming \
-D mapred.reduce.tasks=1 \
-input data/output1/mr3_pr*/* \
-output data/output1/mr3_join \
-mapper mr3_join_mapper.py \
-reducer mr3_join_reducer.py \
-file hadoop1/script1/mr3_join_mapper.py \
-file hadoop1/script1/mr3_join_reducer.py
```

| product_id | description         | price  |
|------------|---------------------|--------|
| 1          | Картофель, кг       | 29.96  |
| 1          | Картофель, кг       | 15.43  |
| 2          | Капуста свежая, кг  | 26.03  |
| 3          | Лук репчатый, кг    | 31.87  |
| 5          | Свекла, кг          | 35.32  |
| 6          | Морковь, кг         | 46.43  |
| 7          | Яблоки, кг          | 111.79 |
| 7          | Яблоки, кг          | 127.08 |
| 8          | Апельсины, кг       | 84.82  |
