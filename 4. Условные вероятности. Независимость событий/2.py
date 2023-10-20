# Created by Hannah at 19.10.2023 17:10
all_var = 12 ** 3
need = 0
for i in range(1, 13):
    for j in range(1, 13):
        for k in range(1, 13):
            if j != i and i != k and j != k and (j == 12 or i == 12 or k == 12):
                need += 1
print(all_var, need, need/all_var)
