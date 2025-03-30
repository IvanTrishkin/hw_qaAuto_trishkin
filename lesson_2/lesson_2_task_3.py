import math

def square(square_side):
    square_area = square_side ** 2
    return math.ceil(square_area)

square_side = float(input("Введите длину стороны квадрата: "))
print(f'Площадь квадрата со стороной {square_side} равна {square(square_side)}')