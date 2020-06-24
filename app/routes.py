from flask import Flask
from flask.views import MethodView


def register_routes(app: Flask, user_view: MethodView):
    app.add_url_rule("/users/",
                     view_func=user_view,
                     methods=["POST"])
    app.add_url_rule("/users/",
                     view_func=user_view,
                     defaults={"user_id": None, },
                     methods=["GET"])
    app.add_url_rule("/users/<string:user_id>",
                     view_func=user_view,
                     methods=["GET", "PUT", "DELETE"])
