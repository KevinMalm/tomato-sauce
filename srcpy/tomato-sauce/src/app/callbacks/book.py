from flask import request
from shared.logging import debug, warn
from shared.types import String
from shared.util import from_json
from interface import TomatoInterface, get_interface
from ..constants import RouteConstants, BackendConstants
from structure.rest import RestResult, BookResponse
from ..app import _app, _sock
from result import Ok, Err

debug("Now registering %s", RouteConstants.BOOK_METADATA)


@_app.route(RouteConstants.BOOK_METADATA, methods=[BackendConstants.GET])
def get_book_metadata_route():
    interface: TomatoInterface = get_interface()
    with interface.book() as b:
        return RestResult.ok(
            BookResponse(
                b.book.title,
                b.book.author,
                b.book.summary,
            )
        )


@_app.route(RouteConstants.BOOK_METADATA, methods=[BackendConstants.POST])
def set_book_metadata():
    interface: TomatoInterface = get_interface()
    req: BookResponse = from_json(BookResponse, request.data)
    with interface.book() as b:
        b.book.title = req.title
        b.book.author = req.author
        b.book.summary = req.summary
        return RestResult.ok(BookResponse(b.book.title, b.book.author, b.book.summary))
