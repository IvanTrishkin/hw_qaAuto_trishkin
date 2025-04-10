class Address:
    def __init__(self, zip_code, city, street, house_number, apartment_number):
        if not isinstance(zip_code, int):
            raise TypeError("zip_code должен быть числом")
        if not isinstance(city, str):
            raise TypeError("city должен быть строкой")
        if not isinstance(street, str):
            raise TypeError("street должен быть строкой")
        if not isinstance(house_number, (int, str)):
            raise TypeError("house_number должен быть числом или строкой")
        if not isinstance(apartment_number, (int, str)):
            raise TypeError("apartment_number должен быть числом или строкой")

        self.zip_code = zip_code
        self.city = city
        self.street = street
        self.house_number = house_number
        self.apartment_number = apartment_number
        self.full_address = f"{self.zip_code} г.{self.city}, ул.{self.street}, д.{self.house_number}, кв.{self.apartment_number}"

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        if not isinstance(to_address, Address) or not isinstance(from_address, Address):
            raise TypeError("to_address и from_address должны быть объектами класса Address")
        if not isinstance(cost, (int, float)):
            raise TypeError("cost должен быть числом")
        if not isinstance(track, str):
            raise TypeError("track должен быть строкой")

        self.to_adress = to_address
        self.from_adress = from_address
        self.cost = cost
        self.track = track
        self.mailing_info = f"""
        Отправление {self.track} 
        из {self.from_adress.full_address} 
        в {self.to_adress.full_address} 
        Стоимость доставки: {self.cost} руб"""
