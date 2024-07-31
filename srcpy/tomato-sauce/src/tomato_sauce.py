from app import _app
from app.constants import BackendConstants
from app.register import register_callbacks, initialize_system
from shared.logging import init_logging, logging


def main():
    def load_demo():
        import os
        from interface import TomatoInterface

        with open(
            os.environ["TOMATO_FILE"],
            "rb",
        ) as f:
            TomatoInterface.open(f)
        return

    init_logging(level=logging.DEBUG)
    initialize_system()
    register_callbacks()
    load_demo()
    _app.run(host=BackendConstants.HOST, port=BackendConstants.PORT)


if __name__ == "__main__":
    main()
