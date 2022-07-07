from project import utils
from project.dao.user_dao import UsersDAO
from project.exceptions import ItemNotFound


class UsersService:
    def __init__(self, user_dao: UsersDAO):
        self.user_dao = user_dao

    def get_by_id(self, uid):
        user = self.user_dao.get_by_id(uid)
        if not user:
            raise ItemNotFound
        return user

    def create(self, email: str, password: str):
        password_hash = utils.generate_user_password(password)
        return self.user_dao.create(email=email, password=password_hash)

    def update_partial(self, user_d):
        user = self.get_by_id(user_d["id"])
        if "name" in user_d:
            user.name = user_d.get("name")
        if "surname" in user_d:
            user.surname = user_d.get("surname")
        if "favourite_genre" in user_d:
            user.favorite_genre = user_d.get("favourite_genre")
        self.user_dao.update(user)

    def update_password(self, user_d):
        user = self.get_by_id(user_d["id"])
        new_password = utils.get_hash_by_password(user_d.get("new_password"))
        old_password_from_db = user.password
        if not utils.compare_passwords(old_password_from_db, utils.get_hash_by_password(user_d.get("old_password"))):
            raise Exception
        user.password = new_password
        self.user_dao.update(user)

    def get_user_by_email(self, email):
        return self.user_dao.get_user_by_email(email)

