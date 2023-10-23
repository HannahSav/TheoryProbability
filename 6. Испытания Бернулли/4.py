# Created by Hannah at 23.10.2023 14:40
import math


def c_a_i(a, i):
    return math.factorial(a)/(math.factorial(a-i)*math.factorial(i))


def count_probability(a):
    res = 0
    p = 0.01
    q = 1-p
    for i in range(1, a+1):
        res += c_a_i(a, i) * p**i * q**(a-i)
    return res


m = 1
p_full = count_probability(m)
print("m = {}, Pm = {}".format(m, p_full))
while p_full < 0.95:
    m += 1
    p_full = count_probability(m)
    print("m = {}, Pm = {}".format(m, p_full))