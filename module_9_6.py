# Домашнее задание по теме "Генераторы"

def all_variants(text):
    for len_t in range(1, len(text) + 1): #перебор длины подстрок от 1 до общ. длины
        for pos_t in range(len(text) - len_t + 1):  #начальные позиции для подстрок
            yield text[pos_t: pos_t + len_t]   #возвращает подстроку от текущей позиции pos_t длиной len_t

a = all_variants ('abc')
for i in a:
    print(i)
print()

a = all_variants ('Deby')
for i in a:
    print(i)