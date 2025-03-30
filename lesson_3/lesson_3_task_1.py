from user import User

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")

my_user = User(first_name, last_name)

my_user.sayName()
my_user.sayLastName()
my_user.sayFullName()