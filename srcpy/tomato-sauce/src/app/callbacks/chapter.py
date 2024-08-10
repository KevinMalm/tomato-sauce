from flask import request
from shared.logging import debug, warn
from shared.types import String
from shared.util import from_json
from interface import TomatoInterface, get_interface
from structure.story.chapter import Chapter
from ..constants import RouteConstants, BackendConstants
from structure.rest import (
    RestResult,
    ListChapterMetadataResponse,
    ChapterContent,
    AddChapterRequest,
    DeleteChapterRequestResponse,
)
from ..app import _app, _sock
from result import Ok, Err

debug("Now registering %s", RouteConstants.BOOK_METADATA)


@_app.route(RouteConstants.LIST_CHAPTER_METADATA, methods=[BackendConstants.GET])
def list_chapter_metadata_route():
    interface: TomatoInterface = get_interface()
    with interface.chapter() as c:
        return RestResult.ok(
            ListChapterMetadataResponse(c.list_all_metadata())
        )  # single record


debug("Now registering %s", RouteConstants.DELETE_CHAPTER)


@_app.route(RouteConstants.DELETE_CHAPTER, methods=[BackendConstants.POST])
def delete_chapter_route():
    interface: TomatoInterface = get_interface()
    failed_options = []
    req: DeleteChapterRequestResponse = from_json(
        DeleteChapterRequestResponse, request.data
    )
    with interface.chapter() as c:
        for id in req.ids:
            match c.delete(id):
                case Err(e):
                    warn(e)
                    failed_options.append(id)
    match len(failed_options):
        case 0:
            return RestResult.ok(DeleteChapterRequestResponse([]))
        case _:
            return RestResult.prompt_error(
                f"Failed to remove {len(failed_options)} Characters",
                ", ".join(failed_options),
            )


debug("Now registering %s", RouteConstants.CHAPTER_CONTENT)


@_app.route(RouteConstants.CHAPTER_CONTENT, methods=[BackendConstants.GET])
def get_chapter_content_route():
    interface: TomatoInterface = get_interface()
    match request.args.get(RouteConstants.CHAPTER_CONTENT_ID_PARAMETER):
        case None:
            msg = (
                f"Failed to parse {RouteConstants.CHAPTER_CONTENT_ID_PARAMETER} in URI"
            )
            warn(msg)
            return RestResult.internal_error(
                "get_chapter_content_route(*)",
                msg,
            )
        case x:
            id = x
    with interface.chapter() as c:
        match c.get_content(id):
            case Err(e):
                warn(e)
                return RestResult.internal_error("get_chapter_content_route(*)", e)
            case Ok(x):
                return RestResult.ok(ChapterContent(String(id), x))


@_app.route(RouteConstants.CHAPTER_CONTENT, methods=[BackendConstants.POST])
def set_chapter_content_route():
    interface: TomatoInterface = get_interface()
    req: ChapterContent = from_json(ChapterContent, request.data)
    with interface.chapter() as c:
        match c.set_content(req.id.string, req.content):
            case Err(e):
                return RestResult.prompt_error("Failed to update Chapter Content", e)
            case Ok(_):
                return RestResult.empty_ok()


@_app.route(RouteConstants.ADD_CHAPTER_METADATA, methods=[BackendConstants.POST])
def add_chapter_metadata_route():
    interface: TomatoInterface = get_interface()
    req: AddChapterRequest = from_json(AddChapterRequest, request.data)
    with interface.chapter() as c:
        match c.add(req.into_chapter()):
            case Err(e):
                return RestResult.prompt_error("Failed to add new Chapter", e)
            case Ok(_):
                return RestResult.ok(
                    ListChapterMetadataResponse(c.list_all_metadata())
                )  # single record
