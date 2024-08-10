from flask_socketio import emit, send
from ..app import _sock
from ..constants import RouteConstants
from shared.util import to_json
from structure.rest import ThinkingState

clients = 0

_thinking_thread = None


@_sock.on("connect")
def socket_connect():
    print("Someone connected")


_workers = 0
_thinking = False


def set_thinking_stage(state: bool, message: str = None):
    global _workers
    global _thinking
    # Worst implementation of a semaphore but ok whatevs

    if state:
        _workers += 1
    else:
        _workers -= 1

    if _workers == 0 and _thinking:
        _thinking = False
        _sock.emit(RouteConstants.THINKING, to_json(ThinkingState(_thinking, message)))
    elif _workers > 0 and _thinking is False:
        _thinking = True
        _sock.emit(RouteConstants.THINKING, to_json(ThinkingState(_thinking, message)))
    return
