from math import log2, ceil

text = 'Пароль 778ППЫЫтттК'
length_of_text = len(text)
alphabet = set('Пароль 778ППЫЫтттК')
length_of_alphabet = len(alphabet)


print('Length of alphabet:', length_of_alphabet, alphabet)

d = {}

for ch in alphabet:
    cnt = text.count(ch)
    print(ch, '->', cnt, '   frequency', round(cnt/length_of_text, 3), '   or  ', cnt, '/', length_of_text)
    d[ch] = cnt;

print('Length of text:', length_of_text)

print(d)

# Вычисляем энтропию
H = 0
for el in d.keys():
    div = d[el] / length_of_text
    H+= div * log2(div)
H = -H
print('H =', H)


n = ceil(log2(length_of_alphabet)) # длина кодовой комбинации при равномерном кодировании. 

L = round((1 - H / n) * 100, 3) # избыточность

print('L = ', L, "%", sep='')
