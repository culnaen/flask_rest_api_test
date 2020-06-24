from typing import Optional
from dataclasses import dataclass


@dataclass
class User:
    name: str
    user_id: Optional[str] = None
