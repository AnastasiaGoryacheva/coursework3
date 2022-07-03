from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegisterView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400, 'Bad Request')
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}


@auth_ns.route('/login/')
class LoginView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get("email")
        password = req_json.get("password")
        if None in (email, password):
            return "", 400

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    def put(self):
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201
