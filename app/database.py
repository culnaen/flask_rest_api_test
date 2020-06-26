import json
from typing import List, Dict, Union
from dataclasses import asdict

from .model import User
from .utils import make_id

Database = Dict[str, Dict[str, str]]


class UserRepository:
    def __init__(self, db: str):
        self.db = db

    def _read(self) -> Database:
        with open(self.db) as f:
            users = json.load(f)
        return users

    def _write(self, data: Database) -> None:
        with open(self.db, "w") as f:
            json.dump(data, f)

    def set(self, user: User) -> Union[str, Dict[str, str]]:
        users = self._read()
        if user.user_id is None:
            user.user_id = make_id()
            result = self._set(users, user)
        else:
            result = self._update(users, user)
        self._write(users)
        return result

    def _set(self, users: Database,  user: User) -> Dict[str, str]:
        user_data = users.setdefault(user.user_id, asdict(user))
        self._write(users)
        return user_data

    def _update(self, users: Database, user: User) -> Union[str, Dict[str, str]]:
        user_data = users.get(user.user_id)
        if user_data is None:
            return "user not found"
        else:
            user_data.update(asdict(user))
            return user_data

    def get_all(self) -> List[Dict[str, str]]:
        users = self._read()
        return list(users.values())

    def get(self, user_id: str) -> Union[str, Dict[str, str]]:
        users = self._read()
        user = users.get(user_id)
        if user is None:
            return "user not found"
        return user

    def delete(self, user_id: str) -> str:
        users = self._read()
        if self._delete(users, user_id):
            self._write(users)
            return "deleted"
        else:
            return "user not found"

    def _delete(self, users: Database, user_id: str):
        try:
            del users[user_id]
        except KeyError:
            return False
        return True
