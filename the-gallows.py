import random

word_list = ['apple', 'banana', 'juice', 'potatoes', 'cheese', 'orange', 'watermelon', 'refrigerator', 'environment', 'pollution', 'happiness', 'mathematics', 'computer', 'device', 'windows', 'hangman', 'bicycle', 'flower', 'snowdrop', 'rose', 'spring', 'chemistry']

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def get_word():
    return random.choice(word_list).upper()


def play(word):
    word_completion = '_' * len(word) 
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        find = input('Введите букву или слово целиком\n').upper()
        
        if len(find) == 1 and find.isalpha():
            if find in guessed_letters:
                print("Вы уже называли букву", find)
            elif find not in word:
                tries-=1
                print(f'Буквы {find} нет в слове, осталось попыток: {tries}')
                guessed_letters.append(find)
            else:
                print(f'Отлично сделано, буква {find} присутствует в слове!')
                guessed_letters.append(find)
                word_as_list = list(word_completion)
                ind = [i for i in range(len(word)) if word[i] == find]
                for i in ind:
                    word_as_list[i] = find
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(find) == len(word) and find.isalpha():
            if find in guessed_words:
                print(f'Вы уже называли слово {find}')
            elif find != word:
                tries -= 1
                print(f'Слово {find} неверно, попробуйте еще раз (Осталось попыток: {tries})')
                guessed_words.append(find)
            else:
                guessed = True
                word_completion = word
        else:
            print('Введите букву или слово')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('YOU WIN, CONGRATULATIONS!!!')
    else:
        print(f'YOU LOSE, the word is {word}, maybe next time')
    


play_again = 'yes'

while play_again[0].lower() == 'y':
    secret = get_word()
    play(secret)
    play_again = input('Play again? (Yes or No)\n')
print('See you soon, bye-bye!')
