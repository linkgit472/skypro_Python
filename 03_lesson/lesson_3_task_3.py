from adress import Adress
from mail import Mailing

adress1 = Adress(119019, 'г.Москва', 'ул.Новый Арбат', 10, 25)
adress2 = Adress(191025, 'г.Санкт-Петербург', 'Невский пр-кт', 45, 12)
mail = Mailing(adress1, adress2, 1267, 10506482037415)

print(f'Отправление {mail.track} из {mail.to_adress.index}, '
      f'{mail.to_adress.city}, {mail.to_adress.street}, {mail.to_adress.home} '
      f'- {mail.to_adress.apt} в {mail.from_adress.index}, '
      f'{mail.from_adress.city}, {mail.from_adress.street}, '
      f'{mail.from_adress.home} - {mail.from_adress.apt}. '
      f'Стоимость {mail.cost} рублей.')
