def month_to_season (month):
    if month in [1,2,12]:
        return 'Зима'
    elif month in [3,4,5]:
        return 'Весна'
    elif month in [6,7,8]:
        return 'Лето'
    elif month in [9,10,11]:
        return 'Осень'
    
def month_input():
    month = int(input('Введите номер месяца: '))
    if month < 1 or month >12:
        print('Некорректный номер месяца')
        return month_input()
    else: 
        return month   
month = month_input()
season = month_to_season(month)
print(f'Месяц {month} относится к сезону {season}.')