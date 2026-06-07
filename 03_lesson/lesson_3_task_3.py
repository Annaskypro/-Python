from address import Address
from mailing import Mailing

address1 = Address("400001", "Волгоград", "Ленина", "100", "100")
address2 = Address("600001", "Москва", "Жукова", "300", "30")
mailing1 = Mailing(address1, address2, 300, 123456)

print(
    f"Отправление {mailing1.track} из {mailing1.from_address} "
    f"в {mailing1.to_address}. Cтоимость {mailing1.cost} рублей."
    )
