from project.Schemas.user_schema import UserSchema
from project.dao.base_dao import BaseDAO
from project.dao.models.user_model import User


class UsersDAO(BaseDAO):
    def get_by_id(self, uid: int):
        user = self.session.query(User).filter(User.id == uid).one_or_none()
        return user

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, email: str, password: str) -> UserSchema:
        new_user = User(
            email=email,
            password=password
        )
        self.session.add(new_user)
        self.session.commit()
        return UserSchema().dump(new_user)

    def update(self, user_data):
        self.session.add(user_data)
        self.session.commit()
