from datetime import date

from rest_framework.exceptions import ValidationError


def check_birth_date(birth_date):
    today = date.today()
    age = (today.year - birth_date.year - 1) + ((today.month, today.day) >= (birth_date.month, birth_date.day))
    if age < 9:
        raise ValidationError(f"Нельзя создать пользователя младше 9 лет. Ваш возраст {age} ")


def check_email(email):
    if "rambler.ru" in email:
        raise ValidationError("Регистрация домена `rambler.ru` запрещена!")
