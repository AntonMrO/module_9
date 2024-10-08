# Домашнее задание по теме "Декораторы"
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        d = 2
        while d * d <= result and result % d != 0 :
            d += 1
        if d * d > result:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a + b + c

print(sum_three(2,3,8))