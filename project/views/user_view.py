from flask import request, abort
from flask_restx import Namespace, Resource

from project import container
from project.Schemas.user_schema import UserSchema
from project.container import user_service
from project.helpers.decorators import auth_required
from project.utils import get_id_from_token

user_ns = Namespace('user')


@user_ns.route("/<int:uid>/")
class UserView(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_by_id(uid)
        result = UserSchema().dump(user)
        return result, 200

    @auth_required
    def patch(self):
        try:
            token = request.headers["Authorization"].split("Bearer ")[-1]
            user_id = get_id_from_token(token)
            req_data = request.json
            req_data["id"] = user_id
            user_service.update_partial(req_data)
        except Exception:
            abort(404, "")
        return "", 200


@user_ns.route("/password/")
class UpdatePassword(Resource):
    @auth_required
    def put(self):
        try:
            token = request.headers["Authorization"].split("Bearer ")[-1]
            user_id = get_id_from_token(token)
            req_data = request.json
            req_data["id"] = user_id
            user_service.update_password(req_data)
        except Exception:
            abort(400, message="Password not change")
        return "Ok", 200
