# Калькулятор на языке Питон
  
# Сложение
def add(num1, num2):
    print(num1, "+", num2, "=", num1 + num2)
    return num1 + num2
  
# Вычитание - subtract
def subtract(num1, num2):
    print(num1, "-", num2, "=", num1 - num2)
    return num1 - num2

# Умножение - multiply
def multiply(num1, num2):
    print(num1, "*", num2, "=", num1 * num2)
    return num1 * num2

# Деление - divide
def divide(num1, num2):
    print(num1, "/", num2, "=", round(num1 / num2, 3))
    return num1 / num2

# Целочисленное деление - int_divide
def int_divide(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    print(num1, "//", num2, "=", num1 // num2)
    return num1 // num2

# Деление по модулю или остаток от деления
def div_mod(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    print(num1, " mod ", num2, "=", num1 % num2)
    return num1 % num2



print("------------КАЛЬКУЛЯТОР НА ЯЗЫКЕ ПИТОН---------")
print("Выберите номер операции -\n" \
        "1. + (сумма)\n" \
        "2. - (вычитание)\n" \
        "3. * (усножение)\n" \
        "4. / (деление)\n" \
        "5. // (целочисленное деление)\n"
        "6. % (остаток от деления)\n")

continue_solving = True
while(continue_solving):
    # Согласно выбранному номеру пользователя
    option = int(input("Выберите операцию 1, 2, 3, 4, 5, 6:\n"))
    # Try - попытаться, проверка на ввод чисел, если не удалось преобразовать в дробное или целое число, 
    # выходит сообщение об ошибке исключение (except)
    try:  
        number_1 = float(input("Введите первое число: "))
        number_2 = float(input("Введите второе число: "))

        # Если введенные числа целые, преобразуем их в целые числа
        if float(number_1) == int(number_1) and float(number_2) == int(number_2):
            number_1 = int(number_1)
            number_2 = int(number_2)
        # Операция по выбранной опции
        if option == 1:
            add(number_1, number_2)
        elif option == 2:
            subtract(number_1, number_2)
        elif option == 3:
            multiply(number_1, number_2)
        elif option == 4:
            divide(number_1, number_2)
        elif option == 5:
            int_divide(number_1, number_2)
        elif option == 6:
            div_mod(number_1, number_2)
        else:
            print("Ошибка, неверный номер операции")
    # Есди введенную строку не удалось преобразоватьт в число, выводится исключение
    except:
        print("Ошибка, введенные данные не являются числами")

    # Условие истинно если ввели единицу, то есть Да в ином случае программа завершается
    continue_solving = (int(input("Хотите продолжить? 1.Да 2.Нет\n")) == 1)

print("************ЗАВЕРШЕНИЕ ПРОГРАММЫ КАЛЬКУЛЯТОРА*************")
