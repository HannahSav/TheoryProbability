# Created by Hannah at 17.10.2023 23:46
import math


def is_prime(a):
    a = abs(a)
    if a < 2:
        return False
    divider = 2
    while divider <= math.ceil(math.sqrt(a)):
        if divider != a and a % divider == 0:
            return False
        divider += 1
    return True


def next_prime(a):
    if a <= 1:
        return 2
    while not is_prime(a):
        a += 1
    return a


def if_div_5(a):
    sum_el = 0
    a = str(a)
    for ch in a:
        sum_el += ord(ch) - ord('0')
    return sum_el % 5 == 0


def if_two_num(a):
    a = str(a)
    return len(a) == 2


def start_with_one(a):
    a = str(a)
    return a[0] == '1'


def all_primes_by(n):
    set_primes = []
    next_start = 2
    while next_start < n:
        next_start = next_prime(next_start)
        set_primes.append(next_start)
        next_start += + 1
    return set_primes


all_pr = all_primes_by(1000)
res = 0
print('Подходящие простые:')
for a in all_pr:
    if if_two_num(a) != if_div_5(a) and not start_with_one(a):
        res += 1
        print(a)
print("Кол-во всех простых до 1000 : {}\nКол-во подходящих : {}\nВероятность : {}".format(len(all_pr), res, res/len(all_pr)))