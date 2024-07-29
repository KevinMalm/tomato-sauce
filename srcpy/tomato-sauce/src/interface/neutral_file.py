from structure.error import InternalConsistencyCheckException


TOMATO_INTERFACE = None


def get_interface():
    global TOMATO_INTERFACE
    if TOMATO_INTERFACE is None:
        raise InternalConsistencyCheckException(
            "tomato_interface",
            "Attempted to access the Global Interface without being set first",
        )
    return TOMATO_INTERFACE


def set_interface(interface):
    global TOMATO_INTERFACE
    TOMATO_INTERFACE = interface
