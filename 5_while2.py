"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {'привет': 'И тебе привет!',
                         'как дела?': 'Отлично, у тебя как?',
                         ('хорошо', 'отлично', 'неплохо'): 'Рад за тебя!',
                         ('чем занимаешься?', 'что делаешь?'): 'Отвечаю на твои вопросы <3!',
                         ('пока', 'всего хорошего', 'до встречи'): 'Пока!'}


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        question_user = input('Введите свой вопрос:\n')
        for key, value in answers_dict.items():
            if isinstance(key, str) and question_user.lower().strip() == key:
                print(value)
            elif isinstance(key, tuple) and question_user.lower().strip() in key:
                if key == ('пока', 'всего хорошего', 'до встречи'):
                    print(value)
                    return
                print(value)


if __name__ == "__main__":
    ask_user(questions_and_answers)
