import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

def generate_password(ln, chars, pass_cnt = 1):
    for j in range(pass_cnt):
        password = ''
        for i in range(ln):
            password += random.choice(chars)
        print('\nВаш пароль: ', password)

def get_info():
    chars = ''
    pass_cnt = int(input('Сколько паролей вы хотели бы сгенерировать?\n'))
    ln = int(input('Введите длину пароля\n'))
    
    include_digits = input('Включить цифры 0-9?  (Yes, No)\n')
    include_lower = input('Включить буквы а-z?  (Yes, No)\n')
    include_upper = input('Включить буквы А-Z?  (Yes, No)\n')
    include_special_symbols = input('Включить специальные символы?  (Yes, No)\n')
    
    same_symbols = input('Исключать ли неоднозначные символы il1Lo0O?  (Yes, No)\n')
    
    if include_digits[0].lower() == 'y': chars+=digits
    if include_lower[0].lower() == 'y': chars+=lowercase_letters
    if include_upper[0].lower() == 'y': chars+=uppercase_letters
    if include_special_symbols[0].lower() == 'y': chars+=punctuation
    if same_symbols[0].lower() == 'y':
        tmp = []
        for el in chars:
            if el not in 'il1Lo0O':
                tmp.append(el)
        chars = tmp
        
    print("Используемые символы: ", list(chars))
    generate_password(ln, chars, pass_cnt)

get_info()
