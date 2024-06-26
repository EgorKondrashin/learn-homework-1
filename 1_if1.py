"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def determine_occupation(age: int):
    if age >= 1 and age <= 3:
        return 'Пользователь ещё слишком юн!'
    elif age >= 4 and age <= 6:
        return 'Пользователь учится в детском саду!'
    elif age >= 7 and age <= 18:
        return 'Пользователь учится в школе!'
    elif age >= 19 and age <= 25:
        return 'Пользователь учится в ВУЗе!'
    elif age >= 26 and age <= 60:
        return 'Пользователь работает!'
    elif age >= 61 and age <= 100:
        return 'Пользователь наслаждается пенсией!'
    else:
        return 'Возраст пользователя должен быть больше 0, но меньше 100!'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Сколько вам лет?\n'))
    result = determine_occupation(age)
    print(result)


if __name__ == "__main__":
    main()
