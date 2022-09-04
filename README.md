# python-some-lang-tips
some language tips 

#### Отсортировать список по последней букве второго элемента
``` Python
items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
sorted_items = sorted(items, key=lambda x: x[-1][-1])  
# sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six')]
```
#### Обратные индексы. Вывести все элементы кортежа countries, кроме двух последних и трех первых.
``` Python
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2])
# ('Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine')
```

#### CSV file reader
``` Python
import csv

cnt = 0
with open("crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

#### Fibonacci using lambda
``` Python
fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))
``` 
#### Заполнение матрицы спиралью

``` Python
rows, cols = map(int, input().split())

matrix = [[0] * cols for _ in range(rows)]

#  0,  1  right
#  1,  0  down
#  0, -1  left
# -1,  0  up
by_row, by_col = 0, 1
r, c = 0, 0

for num in range(1, rows * cols + 1):
    matrix[r][c] = num
    # change direction
    if matrix[(r + by_row) % rows][(c + by_col) % cols]:
        by_row, by_col = by_col, -by_row 
    # move by direction
    r += by_row
    c += by_col
    
[print(*[str(el).ljust(3) for el in row]) for row in matrix]
```
