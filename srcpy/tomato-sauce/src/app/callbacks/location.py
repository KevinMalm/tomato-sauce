from flask import request
from shared.logging import debug
from shared.util import to_json, from_json
from interface import TomatoInterface, get_interface
from ..constants import RouteConstants, BackendConstants
from ..app import _app
from structure.rest import (
    RestResult,
    ListEntitiesResponse,
    DeleteEntitiesRequestResponse,
)
from structure.story import Entity
from result import Err

debug("Now registering %s", RouteConstants.ADD_UPDATE_LOCATION)


@_app.route(
    RouteConstants.ADD_UPDATE_LOCATION,
    methods=[BackendConstants.POST],
)
def update_location_route():
    interface: TomatoInterface = get_interface()
    # update
    location: Entity = from_json(Entity, request.data)
    with interface.location() as c:
        match c.update(location):
            case Err(e):
                return RestResult.prompt_error("Failed to Update Location", e)
    return RestResult.ok(location)


debug("Now registering %s", RouteConstants.DELETE_LOCATION)


@_app.route(
    RouteConstants.DELETE_LOCATION,
    methods=[BackendConstants.POST],
)
def delete_location_route():
    interface: TomatoInterface = get_interface()
    failed_options = []
    req: DeleteEntitiesRequestResponse = from_json(
        DeleteEntitiesRequestResponse, request.data
    )
    with interface.location() as c:
        for id in req.ids:
            match c.delete(id):
                case Err(_):
                    failed_options.append(id)
    match len(failed_options):
        case 0:
            return RestResult.ok(DeleteEntitiesRequestResponse([]))
        case _:
            return RestResult.prompt_error(
                f"Failed to remove {len(failed_options)} Locations",
                ", ".join(failed_options),
            )


debug("Now registering %s", RouteConstants.LIST_LOCATION)


@_app.route(RouteConstants.LIST_LOCATION, methods=[BackendConstants.GET])
def list_locations_route():
    interface: TomatoInterface = get_interface()
    with interface.location() as c:
        return RestResult.ok(ListEntitiesResponse(c.list_all()))  # single record
