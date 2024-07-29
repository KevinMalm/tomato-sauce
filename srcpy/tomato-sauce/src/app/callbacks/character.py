from flask import request
from shared.logging import debug, warn
from shared.util import from_json
from interface import TomatoInterface, get_interface
from ..constants import RouteConstants, BackendConstants
from ..app import _app
from structure.rest import (
    ListEntitiesResponse,
    DeleteEntitiesRequestResponse,
    RestResult,
)
from structure.story import Entity
from result import Err

debug("Now registering %s", RouteConstants.ADD_UPDATE_CHARACTER)


@_app.route(
    RouteConstants.ADD_UPDATE_CHARACTER,
    methods=[BackendConstants.POST],
)
def update_character_route():
    interface: TomatoInterface = get_interface()
    # update
    character: Entity = from_json(Entity, request.data)
    with interface.character() as c:
        match c.update(character):
            case Err(e):
                return RestResult.prompt_error("Failed to Update Character", e)
    return RestResult.ok(character)


debug("Now registering %s", RouteConstants.DELETE_CHARACTER)


@_app.route(
    RouteConstants.DELETE_CHARACTER,
    methods=[BackendConstants.POST],
)
def delete_character_route():
    interface: TomatoInterface = get_interface()
    failed_options = []
    req: DeleteEntitiesRequestResponse = from_json(
        DeleteEntitiesRequestResponse, request.data
    )
    with interface.character() as c:
        for id in req.ids:
            match c.delete(id):
                case Err(e):
                    warn(e)
                    failed_options.append(id)
    match len(failed_options):
        case 0:
            return RestResult.ok(DeleteEntitiesRequestResponse([]))
        case _:
            return RestResult.prompt_error(
                f"Failed to remove {len(failed_options)} Characters",
                ", ".join(failed_options),
            )


debug("Now registering %s", RouteConstants.LIST_CHARACTER)


@_app.route(RouteConstants.LIST_CHARACTER, methods=[BackendConstants.GET])
def list_characters_route():
    interface: TomatoInterface = get_interface()
    with interface.character() as c:
        return RestResult.ok(ListEntitiesResponse(c.list_all()))  # single record
