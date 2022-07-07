from project import utils
from project.dao.auth_dao import AuthDAO


class AuthService:
    def __init__(self, auth_dao: AuthDAO):
        self.auth_dao = auth_dao

    def get_by_email(self, email):
        return self.auth_dao.get_user_by_email(email)

    def login(self, email: str, password: str) -> dict:
        user = self.auth_dao.get_user_by_email(email=email)
        if user is None:
            raise Exception
        password = utils.get_hash_by_password(password)
        if not utils.compare_passwords(user["password"], password):
            raise Exception
        return utils.generate_tokens(user)
