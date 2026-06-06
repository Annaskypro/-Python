from smartphone import Smartphone
catalog = [
    Smartphone("Nokia", "3310", "+79000000000"),
    Smartphone("Samsung", "A50", "+79001111111"),
    Smartphone("Xiaomi", "17 pro", "+79002222222"),
    Smartphone("Xiaomi", "18 pro", "+79003333333"),
    Smartphone("Xiaomi", "19 pro", "+79004444444")
]
for smartphone in catalog:
    print(
        f"{smartphone.brand} - {smartphone.model}. "
        f"{smartphone.subscriber_num}"
    )
