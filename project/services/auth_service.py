from project.dao.auth_dao import AuthDAO
from project.utils import get_hash_by_password, compare_passwords, generate_tokens


class AuthService:
    def __init__(self, auth_dao: AuthDAO):
        self.auth_dao = auth_dao

    def get_by_email(self, email):
        return self.auth_dao.get_user_by_email(email)

    def login(self, email: str, password: str) -> dict:
        user = self.auth_dao.get_user_by_email(email=email)
        if user is None:
            raise Exception
        password = get_hash_by_password(password)
        if not compare_passwords(user["password"], password):
            raise Exception
        return generate_tokens(user)
