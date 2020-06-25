from typing import List, Dict, Union
import json

from .model import User


class UserRepository:
    def __init__(self, db: str):
        self.db = db

    def _read(self) -> Dict[str, Dict[str, str]]:
        with open(self.db) as f:
            users = json.load(f)
        return users

    def _write(self, data) -> None:
        with open(self.db, "w") as f:
            json.dump(data, f)

    def make_id(self):
        with open("count") as f:
            count = int(f.readline().strip()) + 1
        count = str(count)
        with open("count", "w") as f:
            f.write(count)
        return count

    def set(self, user: User) -> Union[str, Dict[str, str]]:
        users = self._read()
        if user.user_id is None:
            user_id = self.make_id()
            result = self._set(users, user_id, user.name)
        else:
            result = self._update(users, user.user_id, user.name)
        self._write(users)
        return result

    def _set(self, users: Dict[str, Dict[str, str]],  user_id: str, name: str) -> Dict[str, str]:
        user = users.setdefault(user_id, {"user_id": user_id, "name": name})
        self._write(users)
        return user

    def _update(self, users: Dict[str, Dict[str, str]], user_id: str, name: str) -> Union[str, Dict[str, str]]:
        user = users.get(user_id)
        if user is None:
            return "user not found"
        else:
            user["name"] = name
            return user

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

    def _delete(self, users: Dict[str, Dict[str, str]], user_id: str):
        try:
            del users[user_id]
        except KeyError:
            return False
        return True


