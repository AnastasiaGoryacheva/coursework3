from project.Schemas.user_schema import UserSchema
from project.dao.auth_dao import AuthDAO
from project.utils import get_hash_by_password, compare_passwords, generate_tokens, generate_new_tokens


class AuthService:
    def __init__(self, auth_dao: AuthDAO):
        self.auth_dao = auth_dao

    def get_by_email(self, email):
        return self.auth_dao.get_user_by_email(email)

    def register(self, email: str, password: str) -> UserSchema:
        password_hash = get_hash_by_password(password)
        return self.auth_dao.create(email=email, password=password_hash)

    def login(self, email: str, password: str) -> dict:
        user = self.auth_dao.get_user_by_email(email=email)
        if user is None:
            raise Exception
        password = get_hash_by_password(password)
        if not compare_passwords(user["password"], password):
            raise Exception
        return generate_tokens(user)

    def update_tokens(self, token):
        return generate_new_tokens(token)
