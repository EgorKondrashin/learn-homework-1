"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def check_string(str1, str2):
    if type(str1) is str and type(str2) is str:
        if str1 == str2:
            return 1
        elif str2 == 'learn':
            return 3
        elif len(str1) > len(str2):
            return 2
    else:
        return 0


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(check_string('1', '1'))  # 1
    print(check_string(1, '1'))  # 0
    print(check_string(1, 1))  # 0
    print(check_string('привет тебе', 'привет'))  # 2
    print(check_string('Python', 'learn'))  # 3
    print(check_string('1', '2'))  # None
    print(check_string('привет', 'привет тебе'))  # None


if __name__ == "__main__":
    main()
