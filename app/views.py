from typing import Union, Dict, Tuple

from flask import request, jsonify
from flask.views import MethodView

from .database import UserRepository
from .model import User

UserResponse = Tuple[Union[str, Dict[str, str]], int]


class UserView(MethodView):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get(self, user_id: str) -> UserResponse:
        if user_id is None:
            result = jsonify(self.user_repository.get_all()), 200
        else:
            result = jsonify(self.user_repository.get(user_id)), 200
        return result

    def post(self) -> UserResponse:
        data = request.get_json()
        if data:
            try:
                user = User(**data)
            except TypeError:
                return jsonify("invalid params"), 400
            result = self.user_repository.set(user), 200
        else:
            result = jsonify("params not specified"), 400
        return result

    def delete(self, user_id: str) -> UserResponse:
        return jsonify(self.user_repository.delete(user_id)), 200

    def put(self, user_id: str) -> UserResponse:
        data = request.get_json()
        if data:
            try:
                user = User(user_id=user_id, **data)
                result = jsonify(self.user_repository.set(user)), 200
            except TypeError:
                result = jsonify("invalid params"), 400
        else:
            result = jsonify("params not specified"), 400
        return result
