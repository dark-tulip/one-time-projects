# Probability Theory and Mathematical Statistics 
# Помощник по расчётно-графической работе

from ordered_set import OrderedSet
from collections import OrderedDict
from math import log, ceil
import numpy as np

# Data of variants set #1.18
s = """
577
554
558
547
555
577
601
555 
568
545
563
595
563
554
561
541 
557
554
563
587
568
552
552
588 
564
571
547
553
586
566
551
558 
547
569
552
548
549
557
561
563 
549
539
562
554
575
551
538
558 
553
549
554
561
564
552
533
572 
578
538
549
564
553
546
547
578 
557
575
575
562
585
584
552
539 
575
566
558
544
592
556
557
556
"""
lst = [int(el) for el in s.split()]

# Множество различных значений
set_lst = OrderedSet(lst)

# словарь
d = {}

# Значеие Х, частота в выборке - P
for el in set_lst:
    d[el] = lst.count(el)

# Cортировка словаря по значениям (keys)
d = OrderedDict(sorted(d.items()))

sample_size_N = len(lst)

# Representive output
print("_____________________START SOLVING________________________")

print("\n----------Вариационный ряд-----------")
lst.sort()
print(*lst)

print("\n{:3s}".format("N_i"), " | ","{:5s}".format("X_i"))
for i in range(sample_size_N):
    print("{:3d}".format(i + 1), " | " ,"{:3d}".format(lst[i]))

print("\n---Cтатистический ряд относительных частот---")
print("   X    N    P")
print(" ________________")
for el in d.keys():
    relative_frequency_P = round(int(d[el])/sample_size_N, 5)

    print("|", el, "|", d[el], "|", relative_frequency_P)
print("There are:", len(d.keys()), "different values")
print("________________")

print("\nМаксимальные и минимальные значения выборки")
x_max = int(max(set_lst))
x_min = int(min(set_lst))

print("X max = ", x_max)
print("X min = ", x_min)

R = x_max - x_min
print("Размах выборки R =", R)

print("Объем выборки N =", sample_size_N, "чисел")

h = (x_max - x_min)/(1 + log(sample_size_N, 2))
print("Величина интервалов по формуле Стерджеса: h =", round(h, 4), "~", ceil(h -0.1))

m = 1 + log(sample_size_N, 2)
print("Число интервалов: m =", round(m, 4), "~", ceil(m))
m = ceil(m)
h = ceil(h - 0.1)

x_initial = x_min - h / 2
print("\nНачало первого интервала:", x_initial)

print("\n----------Интервальный ряд----------")
print("   Range         n_i       p_i     p_i*")
for i in np.arange((x_initial), x_max + 1, int(h)):
    n = 0
    for key, val in d.items():
        if i <= int(key) < i + h:
            n+=val

    print("[", i, " ; ", i + h, ")", " {:4d}".format(n), "     {:.4f}".format(n/sample_size_N), "   ", n, "/", sample_size_N, sep='')

print("\n--------Дискретный статистический ряд--------")
print("(х_i + x_(i+1))/2   n_i   p_i")
# От x_init до x_max, с шагом h 
discrete_dict = {}

for i in np.arange((x_initial), x_max + 1, int(h)):
    n = 0
    for key, val in d.items():
        if i <= int(key) < i + h:
            n+=val
    discrete_dict[((i+i+h) / 2)] = n
    print("\t", (i+i+h) / 2, "{:11d}".format(n), "   {:.4f}".format(n/sample_size_N))

print("\n\n------Эмпирическая функция распределения F(x)-------\n")
lst_frequency_of_elem = [discrete_dict[el] / sample_size_N for el in discrete_dict.keys()]
lst_n_i = [discrete_dict[el] for el in discrete_dict.keys()]
lst_of_elem = [el for el in discrete_dict.keys()]

print(0, 'when ', 'x <=', lst_of_elem[0])
for i in range(1, m):
    print("{:.4f}".format(sum(lst_frequency_of_elem[0:i])), 'when ', lst_of_elem[i - 1], '< x <=', lst_of_elem[i], "or", sum(lst_n_i[0:i]), '/', sample_size_N)

print("{:.4f}".format(sum(lst_frequency_of_elem[0:m])), 'when ', 'x >', lst_of_elem[m - 1])

# X_middle = sum(x_i * n_i) / n
x_middle = sum([float(el) * float(d[el]) for el in d.keys()]) / sample_size_N
print("\nСреднее выборочное значение X_св: ", "{:.4f}".format(x_middle))

# D = sum(n_i * (x_i - x_middle)**2 ) / n
variance = (sum([float(d[el]) * ((float(el) - x_middle)**2) for el in d.keys()]) / sample_size_N)
print("Выборочная дисперсия D_в: ", round(variance, 4))

corrected_variance = variance * sample_size_N / (sample_size_N - 1)
print("Исправленная выборочная дисперсия S**2: ", round(corrected_variance, 4))

# sigma = sqrt(D_в)
sigma = (variance) ** 0.5;
print("\nВыборочное среднеквадратическое отклонение sigma:", round(sigma, 4))

corrected_sigma = (corrected_variance) ** 0.5;
print("Исправленное выборочное среднеквадратическое отклонение S:", round(corrected_sigma, 4))

max_frequency_n = max([d[el] for el in d.keys()])

print("\nНаибольшая частота:", max_frequency_n)
[print("Мода:", M_mode) for M_mode in d.keys() if d[M_mode] == max_frequency_n]

if (sample_size_N % 2 == 1):
    median = lst[sample_size_N // 2]
else:
    x1 = lst[sample_size_N // 2];
    x2 = lst[sample_size_N // 2 - 1];
    print("x1 =", x1);
    print("x2 =", x2);
    median = (x1 + x2) / 2

print("Медиана:", median)

print("\nВыборочный начальный момент \nпри k = 3, M(3) =", "{:.3f}".format(sum([(int(key) ** 3 * int(d[key]) / sample_size_N) for key in d.keys()])))
print("при k = 4, M(4) =", "{:.3f}".format(sum([(int(key) ** 4 * int(d[key]) / sample_size_N) for key in d.keys()])))

M_1 = sum([(int(key) * int(d[key]) / sample_size_N) for key in d.keys()])
m_3 = sum([(int(key) - M_1)**3 * int(d[key]) / sample_size_N for key in d.keys()])
m_4 = sum([(int(key) - M_1)**4 * int(d[key]) / sample_size_N for key in d.keys()])
print("\nВыборочный центральный момент \nпри k = 3, m(3) =", "{:.3f}".format(m_3))
print("при k = 4, m(4) =", "{:.3f}".format(m_4))

print("\nM(1) = выборочному среднему:", "{:.4f}".format(M_1))
m_2 = sum([(int(key) - M_1)**2 * int(d[key]) / sample_size_N for key in d.keys()])
print("m(2) = выборочной дисперсии:", "{:.4f}".format(m_2))

print("Выборочный эксцесс а* =", "{:.4f}".format(m_3 / sigma**3))
print("выборочный коэффициент асимметрии c* =", "{:.4f}".format(m_4 / sigma**4 - 3)) 
