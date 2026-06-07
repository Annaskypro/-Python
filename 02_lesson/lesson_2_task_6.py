lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
print("Числа меньше 30")
for y in range(0, 13):
    if lst[y] < 30:
        print(lst[y])
print("Числа делятся на 3 без остатка")
for y in range(0, 13):
    if lst[y] % 3 == 0:
        print(lst[y])
