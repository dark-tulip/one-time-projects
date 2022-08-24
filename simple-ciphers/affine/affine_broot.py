import itertools


secured_text = 'кцтктэжмлтэржжешхолакцьфрлажтфхшрлацяфъжмжищожцятктмт\
ъцжэвхъжщжэтщкцтктэжмтщкктътцлотъртшуъшуштишъщяррткцтктэжмлкхиохр\
лыхщжхмжхммжыхътцлгжщьъщъцтфждяшкжатчмхшъуафтщшяоьшщяъькцтктэжм\
ляэуъщшбрхшяктоламуыьёякотммсшктщцлчьдяцяфхажфъжвряктътцлякць\
фрлякцтктэжмлрхфхэхсърхомяктфжъхсзжащътоджшмячьищтмтщ'

# Исходный алфавит
ru_alpha_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

alpha_len = len(ru_alpha_letters)
frequncy_disctionary = {}  # cловарь для записи частотного анализа зашифрованного текста

print("Исходный алфавит:")
print(ru_alpha_letters, '\nМощность алфавита N =', alpha_len, 'символов')


for keyletter in ru_alpha_letters:
    frequncy_disctionary[keyletter] = secured_text.count(keyletter) 


# Частотный анализ
print("\nЧастотный анализ cимволов зашифрованного текста")
letters_freq_constants = 'ёъфэщцюшжхйчбэгьыяупдмклврстниаео'  # Позиции частотности символов по убыванию
i = 0

print("[Символ, встречается в зашифрованном тексте, заменяемая буква по индексу частотности]")
sorted_freq_dic = {k: v for k, v in sorted(frequncy_disctionary.items(), key=lambda item: item[1])}
for key in sorted_freq_dic:
    
    print(key, ':', sorted_freq_dic[key], '->', letters_freq_constants[i])
    i+=1


def decrypt(a, b, letter):
    # Позиция символа в алфавите
    letter_pos = ru_alpha_letters.index(letter)
    # a - число обратное a по модулю m
    # b - Число b может принимать любое значение в интервале от 0 до длины алфавита
    return a * (letter_pos - b) % alpha_len


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

a_key_list = [ind for ind in range(alpha_len) if coprime(ind, alpha_len)]
b_key_list = [ind for ind in range(alpha_len)]


print("\nВзаимно простые числа с мощностью алфавита\n", a_key_list, '(Будем использовать для ключа А)')
print(f'\nВозможных вариантов взлома шифра: {len(a_key_list)}x{alpha_len} = {alpha_len * len(a_key_list)}\n')

i = 0

key_combinations = []

# Генерация кортежа возможных вариантов для ключей А и B (Декартово произведение) - B * A
for element in itertools.product(b_key_list, a_key_list):
    key_combinations.append(element)

print(*key_combinations)

print("================================ Начинаем перебор по ключам ===============================")
for combin in key_combinations:
    b, a = combin
    print(f'KEYS A={a}, B={b}\n')

    for letter in secured_text:
        print(ru_alpha_letters[decrypt(a, b, letter)], sep='', end='')
    print('\n\n=========NEXT===========')
    
