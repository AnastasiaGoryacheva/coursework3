import base64
import calendar
import datetime
import hashlib
import hmac
import json
from typing import Union

import jwt
from flask_restx import abort

from project import container
from project.config import BaseConfig



def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def generate_user_password(password):
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        BaseConfig.PWD_HASH_SALT,
        BaseConfig.PWD_HASH_ITERATIONS
    )
    return base64.b64encode(hashed)


def get_hash_by_password(password: str):
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        BaseConfig.PWD_HASH_SALT,
        BaseConfig.PWD_HASH_ITERATIONS
    )
    return base64.b64encode(hashed).decode("utf-8")


def generate_tokens(email, password, is_refresh=False):
    user = container.user_service.get_user_by_email(email)

    if not user:
        raise Exception()

    if not is_refresh:
        if not compare_passwords(user.password, password):
            raise Exception()

    data = {
        "email": user.email
    }
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data['exp'] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.JWT_ALGO)

    days_130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data['exp'] = calendar.timegm(days_130.timetuple())
    refresh_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.JWT_ALGO)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


def compare_passwords(password_hash, password_other):
    return hmac.compare_digest(
        base64.b64decode(password_hash),
        hashlib.pbkdf2_hmac(
            'sha256',
            password_other.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS
        )
    )


def generate_new_tokens(refresh_token):
    data = jwt.decode(jwt=refresh_token, key=BaseConfig.SECRET_KEY, algorithms=BaseConfig.JWT_ALGO)
    email = data["email"]

    user = container.user_service.get_user_by_email(email)

    if not user:
        raise Exception()
    return generate_tokens(user.email, user.password, is_refresh=True)

def decode_token(token: str):
    decoded_token = {}
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=BaseConfig.SECRET_KEY,
            algorithms=[BaseConfig.JWT_ALGO]
            )
    except Exception:
        abort(401)
    return decoded_token


def get_id_from_token(token):
    token = decode_token(token)
    uid = token.get("id")
    return uid
