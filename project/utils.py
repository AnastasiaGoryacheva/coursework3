import base64
import datetime
import hashlib
import hmac
import json
from typing import Union

import jwt
from flask_restx import abort

from project.Schemas.user_schema import UserSchema
from project.config import BaseConfig


def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def generate_user_password(self, password):
    hashed = hashlib.pbkdf2_hmac(hash_name=BaseConfig.HASH_NAME,
                                 salt=BaseConfig.PWD_HASH_SALT.encode("utf-8"),
                                 iterations=BaseConfig.PWD_HASH_ITERATIONS,
                                 password=password.encode("utf-8"))
    return base64.b64encode(hashed)


def get_hash_by_password(password: str):
    hashed = hashlib.pbkdf2_hmac(hash_name=BaseConfig.HASH_NAME,
                                 salt=BaseConfig.PWD_HASH_SALT.encode("utf-8"),
                                 iterations=BaseConfig.PWD_HASH_ITERATIONS,
                                 password=password.encode("utf-8"))
    return base64.b64encode(hashed).decode("utf-8")


def generate_tokens(user: UserSchema):
    payload_access = {
        "email": user["email"],
        "id": user["id"],
        "exp": datetime.utcnow() + datetime.timedelta(minutes=BaseConfig.TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(
        payload=payload_access,
        key=BaseConfig.SECRET_KEY,
        algorithm=BaseConfig.JWT_ALGO
    )

    payload_refresh = {
        "email": user["email"],
        "id": user["id"],
        "exp": datetime.utcnow() + datetime.timedelta(days=BaseConfig.TOKEN_EXPIRE_DAYS)
    }
    refresh_token = jwt.encode(
        payload=payload_refresh,
        key=BaseConfig.SECRET_KEY,
        algorithm=BaseConfig.JWT_ALGO
    )

    tokens = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    return tokens


def compare_passwords(password_hash: str, password_other: str):
    return hmac.compare_digest(password_hash, password_other)


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


def generate_new_tokens(refresh_token):
    decoded_token = decode_token(refresh_token)
    data = {
        "id": decoded_token["id"],
        "email": decoded_token["email"]
    }
    tokens = generate_tokens(data)
    return tokens
