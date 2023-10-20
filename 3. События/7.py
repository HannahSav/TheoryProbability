# Created by Hannah at 17.10.2023 23:46

def counter_all(a):
    if a > 8 ** 2: return None
    res = 1
    n_peres = 1
    for i in range(a):
        res *= (8 ** 2 - i)
        n_peres *= (i + 1)
    return res // n_peres


def counter_cool(a):
    i_dif = 1
    j_dif = 1
    n_peres = 1
    if a > 8: return 0
    for l in range(a):
        i_dif *= (8 - l)
        j_dif *= (8 - l)
        n_peres *= (l + 1)
    return i_dif * j_dif // n_peres


#n = int(input("Введите количество ладей:"))

for n in range(1, 11):
    a = counter_all(n)
    b = counter_cool(n)
    print("Количество всех расстановок {} ладей : {}\nКоличество расстановок {} ладей, не бьющих друг друга : {"
        "}\nВероятность : {}".format(n, a, n, b, b / a))
    print()
