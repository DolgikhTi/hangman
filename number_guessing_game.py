import random  # Подключаем модуль random

def is_valid(num, right):
    """
    Проверяет, что num — это число от 1 до right.
    Возвращает True, если всё ок, иначе False.
    """
    return num.isdigit() and 1 <= int(num) <= right


def play_game():
    print('Добро пожаловать в числовую угадайку!')

    # Пользователь задаёт правую границу
    while True:
        right_border = input('Введите правую границу диапазона (целое число больше 1): ')
        if right_border.isdigit() and int(right_border) > 1:
            right_border = int(right_border)
            break
        else:
            print('Введите корректное число больше 1!')

    # Компьютер загадывает случайное число
    secret = random.randint(1, right_border)
    attempts = 0  # счётчик попыток

    while True:
        user_input = input(f'Введите число от 1 до {right_border}: ')
        if not is_valid(user_input, right_border):
            print(f'А может быть все-таки введем целое число от 1 до {right_border}?')
            continue  # возвращаемся к началу цикла

        user_num = int(user_input)
        attempts += 1

        if user_num < secret:
            print('Ваше число меньше загаданного, попробуйте еще разок.')
        elif user_num > secret:
            print('Ваше число больше загаданного, попробуйте еще разок.')
        else:
            print(f'Вы угадали, поздравляем! 🎉\nВы потратили {attempts} попыток.')
            break  # выход из цикла после победы

    print('Спасибо, что играли в числовую угадайку. Еще увидимся!')


# Основной цикл (возможность повторить игру)
while True:
    play_game()
    again = input('Хотите сыграть ещё раз? (да/нет): ').strip().lower()
    if again not in ('да', 'д', 'yes', 'y'):
        print('До скорой встречи! 👋')
        break
