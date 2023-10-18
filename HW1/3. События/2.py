# Created by Hannah at 17.10.2023 23:53

a = []
for i in range(37):
    a.append(0)

for i in range(1, 13):
    for j in range(1, 13):
        for k in range(1, 13):
            a[i + j + k] += 1

print("сумма : кол-во наборов")
sum = 0
for i in range(2, 37):
    print(i, ':', a[i])
    sum += a[i]

print("сумма : вероятность")
for i in range(2, 37):
    print(i, ":", a[i] / sum)