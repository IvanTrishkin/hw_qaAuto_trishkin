lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

for index, n in enumerate(lst):
    if n % 3 == 0 and n <= 30:
        print(f"Порядковый номер элемента массива: {index}, Число: {n}")