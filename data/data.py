import random


class PersonData:
    user_name = 'Руслан Николаенко'
    login = 'eventautotest@gmail.com'
    password = 'Goodsam74'


class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"