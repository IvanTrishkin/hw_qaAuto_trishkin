def get_year_word(age):
    if 11 <= age % 100 <= 19:
        word = "лет"
    elif age % 10 == 1:
        word = "год"
    elif 2 <= age % 10 <= 4:
        word = "года"
    else:
        word = "лет"
    return word

def print_age(my_age):
    print(f'Сейчас вам {my_age} {get_year_word(my_age)}')

def print_new_age(my_age):
    new_age = my_age + 1
    print(f'А через год вам будет {new_age} {get_year_word(new_age)}')

my_age = int(input("Сколько вам лет? "))

print_age(my_age)

print_new_age(my_age)