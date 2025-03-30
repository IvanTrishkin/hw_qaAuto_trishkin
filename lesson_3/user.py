class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayName(self):
        print(f'Имя пользователя: {self.first_name}')

    def sayLastName(self):
        print(f'Фамилия пользователя: {self.last_name}')

    def sayFullName(self):
        print(f'Полное имя пользователя: {self.first_name} {self.last_name}')