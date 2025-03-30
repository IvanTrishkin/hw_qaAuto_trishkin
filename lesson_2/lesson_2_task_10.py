deposit = float(input ("Введите сумму вклада в рублях: "))

duration = int(input ("Введите срок вклада в годах: "))

rate = 10

def deposit_calculation (deposit, rate, duration):
    for i in range (duration):
        deposit = deposit + deposit * rate / 100
    return deposit

total_deposit = deposit_calculation (deposit, rate, duration)

benefits = total_deposit - deposit

print (f"""Сумма вклада через {duration} лет составит {deposit:.2f} рублей
Заработано за это время {benefits:.2f} рублей""")