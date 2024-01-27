from datetime import datetime, timedelta
import secrets
import string
import random


def generate_date() -> datetime:
    start = datetime(2023, 1, 1)
    end = datetime(2023, 12, 30)

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)

    return start + timedelta(seconds=random_second)


def generate_password() -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(16))
