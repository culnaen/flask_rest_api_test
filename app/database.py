from typing import List, Dict, Optional
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

    def set(self, user: User) -> Dict[str, str]:
        users = self._read()
        if user.user_id is None:
            user_id = str(len(users) + 1)
            return self._set(users, user_id, user.name)
        else:
            return self._set(users, user.user_id, user.name)

    def _set(self, users: Dict[str, Dict[str, str]],  user_id: str, name: str) -> Dict[str, str]:
        user = users.setdefault(user_id, {"user_id": user_id, "name": name})
        user["name"] = name
        self._write(users)
        return user

    def get_all(self) -> List[Dict[str, str]]:
        users = self._read()
        return list(users.values())

    def get(self, user_id: str) -> Optional[Dict[str, str]]:
        users = self._read()
        user = users.get(user_id)
        if user is None:
            return None
        return user

    def delete(self, user_id: str) -> None:
        users = self._read()
        del users[user_id]
        self._write(users)


