from flask import request, jsonify
from flask.views import MethodView

from .database import UserRepository
from .model import User


class UserView(MethodView):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get(self, user_id):
        if user_id is None:
            return jsonify(self.user_repository.get_all())
        return jsonify(self.user_repository.get(user_id))

    def post(self):
        data = request.get_json()
        if data:
            user = User(**data)
            result = self.user_repository.set(user)
            return jsonify(result)

    def delete(self, user_id):
        self.user_repository.delete(user_id)
        return jsonify("deleted")

    def put(self, user_id):
        data = request.get_json()
        user = User(user_id=user_id, name=data["name"])
        result = self.user_repository.set(user)
        return jsonify(result)
