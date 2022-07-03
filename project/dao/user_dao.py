from project.dao.base_dao import BaseDAO
from project.dao.models.user_model import User


class UsersDAO(BaseDAO):
    def get_by_id(self, uid: int):
        user = self.session.query(User).filter(User.id == uid).one_or_none()
        return user

    def update(self, user_data):
        self.session.add(user_data)
        self.session.commit()
