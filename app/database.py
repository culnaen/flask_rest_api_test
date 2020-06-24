from typing import List, Dict
import json

from .model import User


class UserRepository:
    def __init__(self, db: str):
        self.db = db

    def _read(self):
        with open(self.db) as f:
            users: List[Dict[str, str]] = json.load(f)
        return users

    def _write(self, data):
        with open(self.db, "w") as f:
            json.dump(data, f)

    def set(self, user: User):
        users = self._read()
        if user.user_id is None:
            result = self._set(users, len(users) + 1, user.name)
        else:
            result = list(filter(lambda t: t[1]["user_id"] is user.user_id, enumerate(users)))
            if not result:
                result = "Not found this user"
            else:
                result = self._update(users, result, user.name)
        return result

    def get_all(self):
        users = self._read()
        return users

    def get(self, user_id: int):
        users = self._read()
        result = list(filter(lambda u: u["user_id"] is user_id, users))
        if not result:
            result = "Not found this user"
        return result

    def delete(self, user_id: int):
        users = self._read()
        result = list(filter(lambda t: t[1]["user_id"] is user_id, enumerate(users)))
        self._delete(users, result)
        self._write(users)

    def _set(self, users: List[Dict[str, str]], user_id: int, name: str):
        user = {"user_id": user_id, "name": name}
        users.append(user)
        self._write(users)
        return user

    def _update(self, users: List[Dict[str, str]], data: list, name: str):
        user_data, *_ = data
        index, user = user_data
        user = users[index]
        user["name"] = name
        self._write(users)
        return user

    def _delete(self, users: list, data: list):
        user_data, *_ = data
        index, user = user_data
        del users[index]
