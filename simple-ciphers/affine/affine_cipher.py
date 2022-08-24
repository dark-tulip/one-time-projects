from prettytable import PrettyTable


class ConsoleColor:
    # Color
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GRAY = '\033[97m'

    # Style
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # BackgroundColor
    BgBLACK = '\033[40m'
    BgRED = '\033[41m'
    BgGREEN = '\033[42m'
    BgORANGE = '\033[43m'
    BgBLUE = '\033[44m'
    BgPURPLE = '\033[45m'
    BgCYAN = '\033[46m'
    BgGRAY = '\033[47m'

    # End
    END = '\033[0m'


print(ConsoleColor.CYAN + "\n----------------------------ПРОГРАМММА \"АФФИННЫЙ ШИФР\"-----------------------------\n" + ConsoleColor.END)
 

def gcd(a, b):
    # Greatest common divider
    return a if b == 0 else gcd(b, a % b)
 

def solve_decryption_coeff(a, n):
    # коэффициент для обратного шифрования 
    for i in range(1, n):
        if (i * a % n) == 1:
            return i
 

def f(x, a = 5, b = 15, n = 32):
    '''функция шифрования, берем два взаимопростых числа с длиной алфавита'''
    return (a * x + b) % n
 

def f_decryption(x, a = 5, b = 15, n = 32):
    """x means encrypted alpha number"""
    coef = solve_decryption_coeff(a, n)
    return (coef * (x + n - b)) % n
 

print("Длина текста: " + str(len('Деньгииверавсегдабылисильноймотивацией')))
 
text = 'Деньгииверавсегдабылисильноймотивацией'
 
a = ord('а')
alpha_list = [chr(i) for i in range(a, a + 32)]
 
print("Исходный текст")
print("Затем добавим номера букв в алфавите")

table = PrettyTable()
table.field_names = range(len(text))
table.add_row([el for el in text]) 
table.add_row([alpha_list.index(sym.lower()) for sym in text])
print(table)

 
print("\n\nВзаимо простые числа с длиной алфавита, 32:")
for i in range(32):
    if gcd(i, 32) == 1:
        print(i, end = ' ') 
 
print("\n")

enc_table = PrettyTable()
enc_table.field_names = range(len(text))
enc_table.add_row([el for el in text])
 

print(ConsoleColor.YELLOW + "0. Открытый текст")
print("1. Порядковый номер символов открытого текста")
print("2. Применяем функцию шифрования и получаем номера:")
print("3. Заменяем на буквы:" + ConsoleColor.END)


enc_table.add_row([alpha_list.index(sym.lower()) for sym in text])
enc_table.add_row([f(alpha_list.index(sym.lower())) for sym in text])
enc_table.add_row([ConsoleColor.BOLD + alpha_list[f(alpha_list.index(sym.lower()))] + ConsoleColor.END for sym in text])


fieldname = ConsoleColor.GREEN + 'N' + ConsoleColor.END
enc_table._field_names.insert(0, fieldname) 
enc_table._align[fieldname] = 'c' 
enc_table._valign[fieldname] = 't' 

for i, _ in enumerate(enc_table._rows): 
    enc_table._rows[i].insert(0, (ConsoleColor.GREEN + str(i) + ConsoleColor.END) )


secured_text = [alpha_list[f(alpha_list.index(sym.lower()))] for sym in text]
print(enc_table)


print("\nПолучили шифртекст:")
print(ConsoleColor.GREEN + ''.join(secured_text) + ConsoleColor.END )
 
print("\nСчитываем коэффициент для дешифрования:", solve_decryption_coeff(a = 5, n = len(alpha_list)))
 
print("Дешифрование текста:")

dec_table = PrettyTable()
dec_table.field_names = range(len(text))
dec_table.add_row([alpha_list[f_decryption(f(alpha_list.index(sym.lower())))] for sym in text])

print(dec_table)
