def print_list(lst):
    print()
    print("positions: ", end=" ")
    for i in range(len(lst)):
        print('{0:2d}'.format(i + 1), end="  ")
    print()
    print("binary code: ", end="")
    for el in lst:
        print('{0:2s}'.format(el), end="  ")


    control_list = [2 ** i for i in range(5)]
    print("\nNumber:     ", end="")
    for i in range(len(lst)):
        if 2 ** i in control_list:
            print('{0:2d}'.format(2 ** i), end="  ")

    print("\nControl bits:", end="")
    wrong_bit = 0
    for i in range(len(lst)):
        
        if 2 ** i in control_list:
            print('{0:2s}'.format(lst[i]), end="  ")
            if(lst[i] == '1'):
                wrong_bit+=(2 ** i)
    print("\nControl bit summary", wrong_bit)
    print()



[print(el, "digital code:", ord(el), "binary code", '0' + bin(ord(el))[2::]) for el in "LaIs"]

bin_lst = ['0' + bin(ord(el))[2::] for el in "LaIs"]
blst2 = [bin_lst[0] + bin_lst[1], bin_lst[2] + bin_lst[3]]

# Этот список делит на два слога для блочного кодирования по 16 бит то есть по два символа
blst2 = [list(el) for el in blst2]

# Просто добавить нули контрольных битов на степенях двойки
for el in blst2:
    for i in range(5):
        el.insert(2 ** i - 1, '0')  # так как индексация в массиве начинается с нуля минусуем единицу
list_contr_bits = []
# Первый контрольный бит   
for el in blst2:
    s = 0
    for i in range(0, len(el), 2):
        s+=int(el[i])
    el[0] = str(s % 2)
    list_contr_bits.append(s)
    
# второй контрольный бит
for el in blst2:
    s = 0
    for i in range(1, len(el) - 1, 4):
        s+=int(el[i])
        s+=int(el[i + 1])
    el[1] = str(s % 2)
    list_contr_bits.append(s)

    
# третий контрольный бит
for el in blst2:
    s = 0
    l = len(el)
    for i in range(3, l, 8):
        for j in range(4):
            if i + j < l:
                s+=int(el[i + j])  
            else: 
                break       
    el[3] = str(s % 2)
    list_contr_bits.append(s)



# Четвертый контрольный бит
for el in blst2:
    s = 0
    l = len(el)
    for i in range(7, l, 16):
        for j in range(8):
            if i + j < l:
                s+=int(el[i + j])  
            else:
                break        
    el[7] = str(s % 2)
    list_contr_bits.append(s)


# Пятый контрольный бит
for el in blst2:
    s = 0
    l = len(el)
    for i in range(15, l, 16):
        for j in range(16):
            if i + j < l:
                s+=int(el[i + j])
            else:
                break       
    el[15] = str(s % 2)
    list_contr_bits.append(s)





print("Первый этап, вычисление контрольных бит для двух блоков")

for el in blst2:
    print_list(el)
    break

print("Колво единиц в первом слоге контр бит")
list_contr_bits = list_contr_bits[::2]

[print(el, end='  ') for el in list_contr_bits]
list_cont_bits = []
print()

#Ошибочный бит пусть будет на 4 месте
for el in blst2:
    el[3] = '1';
    break;

print("\nafter error fourth(4) bit")
for el in blst2:
    print_list(el)
    break
# Первый контрольный бит   
for el in blst2:
    s = 0
    for i in range(0, len(el), 2):
        s+=int(el[i])
    el[0] = str(s % 2)
    list_cont_bits.append(s)
    break
    
# второй контрольный бит
for el in blst2:
    s = 0
    for i in range(1, len(el) - 1, 4):
        s+=int(el[i])
        s+=int(el[i + 1])
    el[1] = str(s % 2)
    list_cont_bits.append(s)
    break

    
# третий контрольный бит
cont = 0
for el in blst2:
    s = 0
    l = len(el)
    for i in range(3, l, 8):
        for j in range(4):
            if i + j < l:
                s+=int(el[i + j])  
            else: 
                break 
          
    el[3] = str(s % 2)
    list_cont_bits.append(s)
    break



# Четвертый контрольный бит
for el in blst2:
    s = 0
    l = len(el)
    for i in range(7, l, 16):
        for j in range(8):
            if i + j < l:
                s+=int(el[i + j])  
            else:
                break        
    el[7] = str(s % 2)
    list_cont_bits.append(s)
    break

# Пятый контрольный бит
for el in blst2:
    s = 0
    l = len(el)
    for i in range(15, l, 16):
        for j in range(16):
            if i + j < l:
                s+=int(el[i + j])
            else:
                break       
    el[15] = str(s % 2)
    list_cont_bits.append(s)
    break

print("Обратно вычисляем контрольные биты \"La\"")
for el in blst2:
    print_list(el)
    break
print("Колво единиц в первом слоге контр бит")
[print(el, end='  ') for el in list_cont_bits]
print()
summary = 0
print('Суммируем не совпадающие номера ')
for i in range(5):
    if list_cont_bits[i] != list_contr_bits[i]:
        print(2 ** i, end='')
        summary+=(2 ** i)
        if i < 4:
            print(' + ', end='')
print(' =', summary)

if summary > l:
    print("Ошибка, ошибочный бит превысил информационный блок, сравниваем контрольные биты ")
    diff_list=[]
    bin_contr_list=[]
    for i in range(5):
        print(list_contr_bits[i], " ", list_cont_bits[i], end="\n") 
        diff_list.append(0 if list_contr_bits[i] == list_cont_bits[i] else 1)
        bin_contr_list.append(1 if list_contr_bits[i] % 2 else 0)    
    print("Переведем контрольные биты в бинарный вид:")
    print("Разница не равных позиций  ", diff_list)
    print("Начальные контрольные биты ", bin_contr_list)
    print("Разница на этой позиции, значит номер ошибочного контрольного бита:")
    for i in range(5):
        if (diff_list[i] != bin_contr_list[i]):
            print(i + 1, "находящийся под номером разряда", 2 ** i)
