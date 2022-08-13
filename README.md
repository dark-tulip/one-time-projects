# python-some-lang-tips
some language tips 

#### Отсортировать список по последней букве второго элемента
``` Python
items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
sorted_items = sorted(items, key=lambda x: x[-1][-1])  
# sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six')]
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
