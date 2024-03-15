# Створити програму - гру "Поле чудес".
# Зареєструватись на github, та створити окремий репозиторій для цього завдання.
#
# 1. Програма буде брати зі списку слів одне рандомне слово.
# 2. Програма буде отримувати від користувача число - кількість спроб вгадати.
# 3. Далі програма буде чекати від користувача або букву, або ціле слово.
# 4. Якщо користувач пише слово, програма повинна перевіряти чи це не те саме число,
# якщо так то говорити що користувач вгадав слово, або писати що слово не правильне.
# 5. Якщо користувач ввів літеру, програма повинна перевірити чи є ця літера у нашому слові,
# та якщо є, виводити наше слово, де зірочками будуть закриті всі літери, які користувач ще не вгадав,
# або "Такої літери немає".
# 6. Якщо кількість спроб закінчиться, потрібно сказати користувачю, що він програв та закінчити роботу програми.
# 7. Спроби які являється вірними не мають враховуватись в лічильнику.

from random import choice


def random_fruit():
    list_fruits = [
        'apple', 'banana', 'orange', 'lemon', 'kiwi', 'pineapple', 'watermelon', 'grape', 'pear', 'mango', 'avocado',
        'melon', 'peach', 'tangerine', 'nectarine', 'papaya', 'plum', 'pomelo', 'pomegranate', 'apricot'
    ]
    choice_fruit = choice(list_fruits).lower()
    return choice_fruit


fruit = random_fruit()
secret_word = '*' * len(fruit)
guessed_letters = list()

user_attempts = int(input('Enter the number of attempts: '))

while user_attempts > 0:
    user_input = input('Enter a word or letter: ').lower()

    if len(user_input) == 1:
        if user_input in fruit:
            if user_input not in guessed_letters:
                guessed_letters.append(user_input)
                secret_word = ''.join([user_input if user_input in guessed_letters else '*' for user_input in fruit])
                print(secret_word)
                if '*' not in secret_word:
                    print('Congratulations, you guessed the word!')
                    break
            else:
                print('You have already entered this letter!')
        else:
            print('This letter is not in the word!')
            user_attempts -= 1
    elif user_input == fruit:
        print('Congratulations, you guessed the word!')
        break
    else:
        print('Not true. Enter a single letter or word!')
        user_attempts -= 1
