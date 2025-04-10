from smartphone import Smartphone

catalog = []

def add_smartphone(brand, model, phone_number):
    smartphone = Smartphone(brand, model, phone_number)
    catalog.append(smartphone)

add_smartphone("Apple", "iPhone 15", "+123456789")
add_smartphone("Samsung", "Galaxy S23", "+987654321")
add_smartphone("Google", "Pixel 8", "+456789123")

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")