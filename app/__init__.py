from flask import Flask

from .views import UserView
from .routes import register_routes
from .database import UserRepository


def create_app():
    app = Flask(__name__)
    register_routes(
        app,
        UserView.as_view(
            "user",
            user_repository=UserRepository("users.json")
        )
    )
    return app
