from prettytable import PrettyTable     # Для красивого вывода в табличку

# n – количество букв в алфавите, 
# mi – буквы открытого текста, 
# ki – буквы ключа. Тогда буквы шифртекста можно получить так:

alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
open_text = 'ПРОГРАММИСТЫ УЕХАЛИ В КОВОРКИНГ'

open_text = ''.join(open_text.split())
keyword = 'АГДЕВСЕА'

print("\nОткрытый текст:")
print(open_text)

def show_table_text(open_text, keyword, msg):
    # Показать пронумерованные буквы текста, ключа в таблицы

    if msg == 1:
        print('\n1) Разложим состовляющие алфавита на части по ключу\n')
    elif msg == 2:
        print('\n2) Зашифрованное сообщение и ключ\n')
    else:
        print('\n3) Обратное шифрование\n')

    table = PrettyTable(range(len(open_text))) # Порядковый номер по буквам заданного текста

    table.add_row(list(open_text))             # Символы открытого текста
    table.add_row(list((keyword * (len(open_text) // len(keyword) + 1))[:len(open_text)])) # Повторение ключа после завершения

    print(table)


def encrypt_vijener(open_text, keyword):
    # Функция для шифрования алгоритмом виженера

    encrypted_text = ''

    for i in range(len(open_text)):
        letter_index = alphabet.index(open_text[i])     # Для каждой буквы из открытого текста
        key_i = alphabet.index(keyword[i % len(keyword)])

        encrypted_text+= str(alphabet[(letter_index + key_i) % len(open_text)]) # Тут прибавляется позиция ключа

    show_table_text(encrypted_text, keyword, 2)
    return encrypted_text


def decrypt_vijener(closed_text, keyword):
    # Обратное шифрование алгоритмом виженера

    decrypted_text = ''

    for i in range(len(closed_text)):                   # Для каждой буквы из зашифрованного текста
        letter_index = alphabet.index(closed_text[i])
        key_i = alphabet.index(keyword[i % len(keyword)])

        decrypted_text+= str(alphabet[(letter_index - key_i) % len(closed_text)]) # Тут отнимается позиция ключа

    show_table_text(decrypted_text, keyword, 3)
    return decrypted_text



show_table_text(open_text, keyword, 1)

encrypted_text = encrypt_vijener(open_text, keyword)

decrypt_vijener(encrypted_text, keyword)