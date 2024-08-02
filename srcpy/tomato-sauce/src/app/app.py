from app.constants import BackendConstants
from flask import Flask, request, make_response

# from flask_sock import Sock
from flask_socketio import SocketIO

_app = Flask(
    __name__,
)

# _sock = Sock(_app)
_sock = SocketIO(_app, cors_allowed_origins="*")


@_app.after_request
def after_request_func(response):
    origin = request.headers.get("Origin")
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.add("Content-Type", "application/json")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, PATCH, DELETE"
        )
        response.headers.add("Access-Control-Allow-Origin", "*")
    else:
        response.headers.add("Access-Control-Allow-Credentials", "true")
        if origin:
            response.headers.add("Access-Control-Allow-Origin", origin)

    return response
