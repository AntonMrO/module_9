#Домашнее задание по теме "Создание функций на лету"
# 1. Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x==y, first, second)))
#[False, True, True, False, False, False, False, False, True, False, False, False, False, False]

# 2.Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with (open(file_name, 'w', encoding='utf-8') as file):
            for elem in data_set:
                print(elem)
                file.writelines(f'{str(elem)}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# 3.Метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
