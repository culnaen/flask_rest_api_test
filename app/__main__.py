from flask import Flask

import app.config as config

from app.views import UserView
from app.routes import register_routes
from app.database import UserRepository


def create_app(path_to_db):
    app = Flask(__name__)
    register_routes(
        app,
        UserView.as_view(
            "user",
            user_repository=UserRepository(path_to_db)
        )
    )
    return app


if __name__ == '__main__':
    app = create_app(config.PATH_TO_DB)
    app.run()
