from smartphone import Smartphone

phone1 = Smartphone('iphone', '15 pro', '+79001234567')
phone2 = Smartphone('iphone', '17', '+79520129876')
phone3 = Smartphone('samsung', 'A67', '+79110781235')
phone4 = Smartphone('samsung', 'S24 FE', '+79113247683')
phone5 = Smartphone('samsung', 'Z flip 7', '+79110547683')

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(f'{phone.marka} - {phone.model}. {phone.number}')
