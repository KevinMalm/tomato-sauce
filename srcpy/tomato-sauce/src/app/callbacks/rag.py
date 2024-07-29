from interface import TomatoInterface, get_interface
from ..constants import RouteConstants, BackendConstants
from ..app import _app
from shared.logging import debug
from result import Ok, Err
from structure.rest import RestResult

debug("Now registering %s", RouteConstants.RAG_REFERENCES)


@_app.route(RouteConstants.RAG_REFERENCES, methods=[BackendConstants.GET])
def llm_references():
    interface: TomatoInterface = get_interface()

    match interface.last_references():
        case Err(e):
            return RestResult.prompt_error("Missing Data for your Request", e)
        case Ok(x):
            return RestResult.ok(x)
