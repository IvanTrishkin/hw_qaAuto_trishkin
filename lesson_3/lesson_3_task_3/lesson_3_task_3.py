from mailing import Address, Mailing
import random
import string

store_zip_code = 108235
store_city = "Москва"
store_street = "Ленина"
store_house_number = 52
store_apartment_number = 45

to_zip_code = int(input('Введите ваш индекс: '))
to_city = (input('Введите ваш город: '))
to_street = (input('Введите вашу улицу: '))
to_house_number = input('Введите ваш номер дома: ')
to_apartment_number = input('Введите ваш номер квартиры: ')

store_address = Address (store_zip_code, store_city, store_street, store_house_number, store_apartment_number)
to_address = Address (to_zip_code, to_city, to_street, to_house_number, to_apartment_number)

def generate_tracking_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

tracking_number = generate_tracking_number()

first_mailing = Mailing(to_address, store_address, 500, tracking_number)



print(f'Адрес получения: {to_address.full_address}')
print(f'Адрес отправления: {store_address.full_address}')
print(f'''Информация о отправлении:
{first_mailing.mailing_info}''')