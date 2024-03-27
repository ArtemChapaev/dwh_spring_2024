## Задание

Собрать статистику по числу знаков препинания в строке. Формат вывода: 
`f"{punctuation_mark}:{lines_count}:{count}"` - где `lines_count` - число строк, 
в которых появился знак препинания, `count` - количество вхождений в текст. 
Вывод отсортировать по количеству вхождений.


## Решение

В качестве знаков препинания я выбрал следующие знаки - `.,?;:!-"\'()[]{}<>`.


Для решения моей задачи, я написал mapper, в котором считываю строку, затем создаю 
объект `collections.Counter`. Объект такого класса позволяет быстро получить 
количество нужных знаков в текущей строке, если оно не 0, то я вывожу строку 
`{punctuation_mark}\t1\t{count}`.


На части reducer'а я в первую очередь считываю вывод mapper'а, а затем решаю задачу 
сортировки. Сначала я сохраняю в массив все элементы, тк их количество заранее 
определено и не велико. Затем сортирую и вывожу в правильном порядке.

## Примеры

Рассмотрим простой случай, для файла `data/data1/wctest.txt`, где на 3 строках по 
2 запятые. То есть мы будем ожидать следующий вывод `,:3:6`. Проверим

```
mapred streaming \
-D mapred.reduce.tasks=1 \
-input data/data1/wctest.txt \
-output data/output1/mr4_agg_test \
-mapper mr4_agg_mapper.py \
-reducer mr4_agg_reducer.py \
-file hadoop1/script1/mr4_agg_mapper.py \
-file hadoop1/script1/mr4_agg_reducer.py
```

Тогда в файле `data/output1/mr4_agg_test` найдем следующую запись:
```
,:3:6	
```

Применим указанный MapReduce для файлов из директории `books`:

```
mapred streaming \
-D mapred.reduce.tasks=1 \
-input data/data1/books/* \
-output data/output1/mr4_agg_books \
-mapper mr4_agg_mapper.py \
-reducer mr4_agg_reducer.py \
-file hadoop1/script1/mr4_agg_mapper.py \
-file hadoop1/script1/mr4_agg_reducer.py
```

Тогда получим в файле следующее:

```
,:18474:27664
.:14419:16353
-:2352:3829
;:3485:3618
':1795:2025
!:1446:1694
?:1489:1595
::487:495
(:222:228
):221:228
":14:22
[:6:6
```
