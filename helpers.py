import requests
from faker import Faker
import random
import string
from urls import *

def unique_user_data():
    fake = Faker()
    email = fake.email()

    password_chars = [random.choice(string.ascii_letters) for _ in range(6)]
    password_chars.append(random.choice(string.digits))
    password_chars.append(random.choice(string.punctuation))
    random.shuffle(password_chars)
    password = "".join(password_chars)

    payload = {
        "email": email,
        "password": password,
        "name": fake.name().split()[0],
    }
    return payload


def registered_user(user_data):
    res = requests.post(USER_REGISTER_URL, json=user_data)
    assert res.status_code == 200, f"Не удалось зарегистрировать пользователя: {res.text}"
    data = res.json()
    access_token = data["accessToken"].split()[1]
    refresh_token = data.get("refreshToken")
    token_header = {"Authorization": f"Bearer {access_token}"}
    return {
        **user_data,
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_header": token_header,
    }


def delete_user(token_header):
    res = requests.delete(USER_DATA_URL, headers=token_header)
    assert res.status_code in (200, 202, 204, 401), f"Ошибка при удалении пользователя: {res.status_code} {res.text}"
