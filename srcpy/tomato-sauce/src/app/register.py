from app.app import _app
from shared.logging import info


def register_callbacks():
    info("Now Registering all Callbacks...")
    from .callbacks.character import (
        update_character_route,
        delete_character_route,
        list_characters_route,
    )
    from .callbacks.location import (
        update_location_route,
        delete_location_route,
        list_locations_route,
    )
    from .callbacks.chapter import list_chapter_metadata_route
    from .callbacks.chat import llm_chat
    from .callbacks.rag import llm_references

    info("Done Registering all Callbacks")
    return


def initialize_system():
    info("Now Initializing System Data...")
    info("Done Initializing System Data")
    return
