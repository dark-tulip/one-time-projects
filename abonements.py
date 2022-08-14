import random

def print_sorted_abonements(abon_list):
    name_dict = {}
    name_list = []
    index = 0
    for abon in abon_list:
        name_dict[abon.name] = index
        name_list.append(abon.name)
        index+=1
    name_list.sort()
    for abon in name_list:
        abonement = abon_list[name_dict[abon]]
        print('{:8s}'.format(abonement.name), "phone number:", abonement.phone_number, " Баланс на счету:", abonement.balance)
    print("\nКоличество выведенных абонементов", index)
    

def find_with_minus_sum(abon_list):
    for abonement in abon_list:
        if abonement.balance < 0:
            print('{:8s}'.format(abonement.name), "у вас отрицательный остаток на счету", abonement.balance, "тг")


def find_abon_by_number(abon_list, digits_list):
    cnt = 0
    for abonement in abon_list:
        isTrue = True
        for digit in digits_list:
            if digit not in abonement.phone_number:
                isTrue = False
                break
        if not isTrue:
            continue
        cnt+=1
        print('{:8s}'.format(abonement.name), "was found with this phone number:", abonement.phone_number)
    print("Найдено", cnt, "абонентов")
    

def generate_phone_number():
    """
    This function generates random phone number
    """
    number = "8"
    number += "(" + str(random.randint(700, 800)) + ")"
    number += " " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    number += " " + str(random.randint(0, 9)) + str(random.randint(0, 9))
    number += " " + str(random.randint(0, 9)) + str(random.randint(0, 9))
    return number


def generate_applying_date():
    """
    This function generates random applying date
    """
    applying_date = str(random.randint(2000, 2020)) + ":"
    applying_date += "{:02d}".format(random.randint(1, 12)) + ":"
    applying_date += "{:02d}".format(random.randint(1, 30))
    return applying_date


class Abonement:
    # конструктор
    def __init__(self, name, phone_number, applying_date, tarif, balance):
        self.name = name  # устанавливаем имя
        self.phone_number = phone_number   # номер телефона
        self.applying_date = applying_date    # дата подключения к связи
        self.tarif = tarif   # сумма абонентской платы
        self.balance = balance    # остаток на счету

 
    def __del__(self):
        print(self.name,"удален из памяти")
    

    def get_information(self):
        """
        This functions prints information about abonement
        """
        print("\n-----Information about abonement-----\n")
        print("ФИО абонента:     ", self.name)
        print("Номер телефона:   ", self.phone_number)
        print("Дата подключения: ", self.applying_date)
        print("Абонентская плата:", str(self.tarif) + "тг")
        print("Остаток на счету: ", str(self.balance) + "тг\n")


    def print_with_minus_balance(self):
        """
        This fucntion shows abonents with minus balance
        """
        if self.balance < 0:
            print(self.name + ",", "Ваш баланс:", self.balance, "тг, пожалуйста пополните ваш счет")
            return 1
        return 0
        
    

    def add_price(self):
        """
        This fucntion adds 200 money to abonents, applyed greater than 10 years
        """
        now = self.applying_date.split(':')
        if 2020 - int(now[0]) >= 10:   # we get its applying year
            self.balance +=200
            print('{:8s}'.format(self.name), "Спасибо что вы с нами уже 10 лет, вам начислено 200тг! Остаток на счету:", self.balance, "тг")            

    
    def apply_to_tarif(self):
        """
        This function checks, if abonement has apply to tarif with balance
        """
        if self.balance >= self.tarif:
            self.balance-=self.tarif
            print('{:8s}'.format(self.name), "Cпасибо что вы с нами, снята абонентская плата за тариф", self.tarif, "тг", "Остаток на счету:", self.balance, "тг")
        else:
            print('{:8s}'.format(self.name), "На счету недостаточно средств, пожалуйста пополните баланс для подключения тарифа")


tarif_list = [2390, 1890, 790, 5990, 4990, 1590, 990, 3690]
person_list = ["Aidyn", "Asem", "Ainur", "Arman", "Amina", "Anel", "Bolat", "Berik", "Makpal", "Madina", "User", "Eldos"]

abonement_list = []

print("----------Полный список всех абониментов----------")
for i in range(len(person_list)):
    abonement_list.append(Abonement(person_list[i],  generate_phone_number(), generate_applying_date(), random.choice(tarif_list), random.randint(-1000, 6000)))
    abonement_list[i].get_information()

print("----------Абонента с каким номером вы хоиите найти?----------")
phone_list = [el for el in input()]
find_abon_by_number(abonement_list, phone_list)

print("\n----------Начисляем призовой баланс абонентам----------")
for i in range(len(person_list)):
    abonement_list[i].add_price()

print("\n----------Снимаем абонентскую плату за месяц----------")
for i in range(len(person_list)):
    abonement_list[i].apply_to_tarif()

print("\n----------Выведем список людей с отрицательным балансом----------")
find_with_minus_sum(abonement_list)

print("\n----------Выведем отсортированный список абонентов----------")
print_sorted_abonements(abonement_list)
