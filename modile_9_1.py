# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([0.5, 6, 20, 15, 9, 33.2, 13.3, 55, 6, 76], len, sum, sorted, min))

