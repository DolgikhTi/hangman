import random

word_list = ['ПИТОН', 'ПРОГРАММА', 'КОМПЬЮТЕР', 'АЛГОРИТМ', 'ФУНКЦИЯ', 'ИГРА', 'ЦИКЛ', 'ПЕРЕМЕННАЯ']

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
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

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input("Введите букву или слово целиком: ").upper()

        if not guess.isalpha():
            print("Ошибка: нужно вводить только буквы!")
            continue

        # Если пользователь ввел одну букву
        if len(guess) == 1:
            if guess in guessed_letters:
                print("Вы уже называли эту букву:", guess)
            elif guess not in word:
                print("Буквы", guess, "нет в слове.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Отлично! Буква", guess, "есть в слове!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            # Если пользователь вводит всё слово
            if guess in guessed_words:
                print("Вы уже пробовали слово:", guess)
            elif guess != word:
                print("Слово", guess, "не верное.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        print(display_hangman(tries))
        print(word_completion)
        print()

    if guessed:
        print("Поздравляем, вы угадали слово! Вы победили!")
    else:
        print("Вы проиграли. Загаданное слово было:", word)

def main():
    while True:
        word = get_word()
        play(word)
        again = input("Хотите сыграть ещё раз? (д/н): ").lower()
        if again != 'д':
            print("Спасибо за игру! До встречи!")
            break

if __name__ == "__main__":
    main()
