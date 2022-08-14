from random import choice

# clubs, diamonds, hearts, or spades (Обозначены как C, D, H, S)
# Входные данные 10C JC QC KC 
cards_str = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']   # значения
cards_colours = ['C', 'D', 'H', 'S']

cards_lst = []   # Список комбинаций 52 карт

# Генерируем колоду 52-карт
for el in cards_str:
    for elem in cards_colours:
        cards_lst.append(str(el) + str(elem))

print('Список колоды карт:\n', cards_lst)
l = ["High Card", "Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

print("\nПриоритет выигрышных комбинаций, по возрастанию:\n", l)
# Рандомно выбираем карты машине
machines_cards = []
for i in range(5):
    machines_cards.append(choice(cards_lst))
    cards_lst.pop(cards_lst.index(machines_cards[i]))

# Рандомно выбираем карты пользователю
users_cards = []
for i in range(5):
    users_cards.append(choice(cards_lst))
    cards_lst.pop(cards_lst.index(users_cards[i])) # Удаляем из колоды карт выборанные карты


# Если пользователь хочет поменять одну карту
print("\nВаши карты:", users_cards)
answer = int(input('Хотите поменять карты?\nВведите 1 если да, 2 если нет: '))
if (answer == 1):
    replcae_num = int(input('Какую карту поменять? Введите номер 1,2,3,4,5\nНомер: ')) - 1
    cards_lst.append(users_cards[replcae_num])
    users_cards[replcae_num] = choice(cards_lst)

print("\nВаши карты:", users_cards)



def find_priority(l2):
    V, S = [], []  # VALUES AND SUITS - значения и масти карт 
    for el in l2:  # Разделяем значения и масти карт 
        V.append(el[:-1])
        S.append(el[-1])

    def check_order():
        # Функция для обнаружения Прямого Флеша, когда четыре карты одной масти в числовом порядке.
        for i in range(8):
            if cards_str[i] in V and cards_str[i+1] in V and cards_str[i+2] in V and cards_str[i+3] in V and cards_str[i+4] in V:
                return True
        return False

    def check(V, S):    
        
        if '10' in V and 'J' in V and 'Q' in V and 'K' in V and'A' in V:
            # Royal Flush, Состоит из туза, короля, дамы, валета и десятки одной масти.
            return 9
        
        set_S_len, set_V_len = len(set(S)), len(set(V))
        
        if check_order():
            if set_S_len == 1:
                # Прямой Флеш четыре карт одной масти в числовом порядке.
                return 8
            # Иначе это Straight - Страйк
            return 4
        
        if set_S_len == 1:
            # Flush, флэш содержит четыре карт одной масти
            return 5
        
        if V.count(V[0]) == 4 or V.count(V[1]) == 4:
            # Four of a Kind, Четыре в своем роде, когда Четыре карты с одинаковым значением.
            return 7
        
        if set_V_len == 2:       
            v2 = list(set(V))
            if V.count(v2[0]) == 2 and V.count(v2[1]) == 3 or V.count(v2[1]) == 2 and V.count(v2[0]) == 3:
                # Полный Дом, Фулл Хаус, три карты одинакового достоинства, а оставшиеся две карты образуют пару.
                return 6
                
        if V.count(V[0]) == 3 or V.count(V[1]) == 3 or V.count(V[2]) == 3:
            # Комбинация Three of a Kind, три карты с одинаковым значением
            return 3
        
        if set_V_len <= 3 and [V.count(V[i]) for i in range(5)].count(2) == 4:
            # Two Pairs
            return 2
        
        if set_V_len == 4:
            # Pair
            return 1   
        # не соответствуют какой-либо более комбинационной категории, 
        # ранжируются по значению их старшей карты
        return 0
    return l[check(V, S)]


# print('TEEESSSST ROYAL FLASH COMBINATION', find_priority(['10C','JC', 'QC', 'KC', 'AC']))

user_step = find_priority(users_cards)
print('Ваша комбинация:', user_step)
machine_step = find_priority(machines_cards)
print('Комбинация машины:', machine_step)


if ("High Card" == machine_step and user_step == "High Card"):  # Если не найдено выигрышных комбинаций
    print('Комбинация:', user_step, '\nВычисляем победителя по старшей карте')
    order = 'AKQJTZ98765432'  # Используем Z как номер десятки
    
    # Вырезаем масть из карты, работаем со значениями
    user_hand = ' '.join([el[0:len(el) - 1] for el in users_cards]) 
    user_hand = ''.join(user_hand.replace('10', 'Z').split())
    # Самая большая по приоритету карта пользоватея
    highest_users_card = min(user_hand, key=order.index)

    # Вырезаем масть из карты машины, работаем со значениями
    machine_hand = ' '.join([el[0:len(el) - 1] for el in machines_cards])
    machine_hand = ''.join(machine_hand.replace('10', 'Z').split())

    highest_machine_card = min(machine_hand, key=order.index)

    if highest_users_card == highest_machine_card:
        # Если старшие карты пользователя и машины совпадают
        if user_hand.count(highest_machine_card) == machine_hand.count(highest_machine_card):
            # Если кол-во совпадаемых значений равны
            machine_hand.replace(highest_machine_card, '')
            user_hand.replace(highest_users_card, '')

            highest_users_card = min(user_hand, key=order.index)
            highest_machine_card = min(machine_hand, key=order.index)

    # Сравниваем наивысшие по приоритету карты обоих игроков
    finish = highest_machine_card + highest_users_card

    max_value = min(finish, key=order.index)
    if max_value == highest_users_card:
        print('\nВыиграли карты пользователя: Поздравляем, вы выиграли!!!')
    else:
        print('Выиграли карты машины: Вы проиграли')

else:
    # Если получена какая либо выигрышная комбинация из списка L 
    user_combination  = l.index(user_step)  # Получаем их индекс расположения
    machine_combination = l.index(machine_step)
    print('\n============ВЫИГРАЛА КОМБИНАЦИЯ========')
    # Индекс приоритета больше у пользователя
    if user_combination > machine_combination:
        print(user_step)
        print('\nВыиграли карты пользователя: Поздравляем, вы выиграли!!!')
    elif user_combination == machine_combination:
        # Индекс приоритета равен
        print(machine_step, 'НИЧЬЯ')
    else:
        # Индекс старше у машины
        print(machine_step)
        print('Выиграли карты машины: Вы проиграли')

print("\nВаши карты:", users_cards)
print('Карты машины:', machines_cards)
