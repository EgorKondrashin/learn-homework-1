"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    while True:
        ask_user = input('Как дела?\n')
        if ask_user == 'Хорошо':
            break

    
if __name__ == "__main__":
    hello_user()
