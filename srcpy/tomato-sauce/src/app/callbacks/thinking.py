from flask_socketio import emit, send
from ..app import _sock

clients = 0


@_sock.route("/thinking")
def thinking_check(sock):
    while True:
        data = sock.receive()
        sock.send(data)


# Function that runs when a clients get connected to the server
@_sock.on("connect")
def test_connect():
    global clients
    clients += 1
    print("Client connected test")


# Read data from client
@_sock.on("new-message")
def handle_message(message):
    print("received message" + message)
    send_data()


# Send data to client
@_sock.on("new-message-s")
def send_data():
    data = 1.23
    print("sending Data: temp: {0}, hum: {1}".format(data))
    emit("data-tmp", {"temperature": data})


@_sock.on("disconnect")
def test_disconnect():
    global clients
    clients -= 1
    print("Client disconnected")
