## Задание

Создать внешнюю таблицу на данных `coreDemography` и написать запрос рассчитывающий распределение 
дней рождения по месяцам.

`coreDemography` содержит данные демографии пользователей ОК.

## Создание таблицы

В качестве колонок таблицы используются следующие свойства:
1. id - id пользователя
2. create_date - дата создания профиля
3. birth_date - дата рождения (число дней от 1970-01-01)
4. gender - пол (2 - женщина, 1 - мужчина)
5. id_country - id страны
6. id_location - id местоположения
7. login_region - номер региона

Таким образом, создание внешней таблицы использует следующий запрос:

```SQL
CREATE EXTERNAL TABLE demography (
    demography_id INT,
    create_date BIGINT,
    birth_date INT,
    gender TINYINT,
    id_country BIGINT,
    id_location INT,
    login_region INT
)
row format delimited
fields terminated by '\t'
lines terminated by '\n'
LOCATION '/home/a.chapaev/data/coreDemography';
```

## Выполнение запроса

Для преобразования формата числа дней от 1970-01-01 в привычный формат системы UNIX используется 
функция FROM_UNIXTIME, которая позволяет сразу определить месяц дня рождения. Полностью запрос выглядит следующим образом:

```SQL
SELECT birth_month, count(1) AS cnt FROM (
     SELECT
         FROM_UNIXTIME(birth_date * 86400, 'MM')
     AS birth_month
     from demography
) temp 
group by birth_month
order by birth_month;
```

В результате выполнения запроса были получены следующие данные: 

```text
NULL	9
01	10289
02	8508
03	9236
04	8865
05	9053
06	9347
07	9537
08	9217
09	8659
10	8541
11	8056
12	8248
```

Общее время выполнения запроса - `49.13 seconds`.
