from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import user_service
from project.utils import generate_new_tokens, generate_tokens

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400, 'Bad Request')
        user = user_service.create(
                email=req_json["email"],
                password=req_json["password"]
            )
        return "", 201, {"location": f"/users/{user.id}"}


@auth_ns.route('/login/')
class LoginView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in (email, password):
            return "", 400

        tokens = generate_tokens(email, password)

        return tokens, 201

    def put(self):
        data = request.json
        token = data.get('refresh_token')
        tokens = generate_new_tokens(token)

        return tokens, 201
