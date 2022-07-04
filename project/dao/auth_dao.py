from project.Schemas.user_schema import UserSchema
from project.dao.base_dao import BaseDAO
from project.dao.models.user_model import User


class AuthDAO(BaseDAO):
    def create(self, email: str, password: str) -> UserSchema:
        new_user = User(
            email=email,
            password=password
        )
        self.session.add(new_user)
        self.session.commit()
        return UserSchema().dump(new_user)

    def get_user_by_email(self, email: str) -> UserSchema:
        user = self.session.query(User).filter(User.email == email).one_or_none()
        if user is not None:
            return UserSchema().dump(user)
        return None