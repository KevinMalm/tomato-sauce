from flask import Response, request
from interface import TomatoInterface, get_interface, PromptTag
from ..constants import RouteConstants, BackendConstants
from ..app import _app
from shared.logging import debug, warn
from shared.util import from_json
from structure.rest import ChatConversation

debug("Now registering %s", RouteConstants.CHAT)


@_app.route(RouteConstants.CHAT, methods=[BackendConstants.POST])
def llm_chat():
    MESSAGE_TAG = "message"
    CONTENT_TAG = "content"
    interface: TomatoInterface = get_interface()
    req: ChatConversation = from_json(ChatConversation, request.data)

    req = interface.prompter(
        PromptTag.StandardChatPrompt if req.inject_rag else PromptTag.NoRAGChatPrompt
    ).inject(req)

    def process(content):
        response = interface.llm.chat(content)
        for res in response:
            yield res[MESSAGE_TAG][CONTENT_TAG].encode(BackendConstants.UTF_8_ENCODING)

    return Response(process(req), mimetype=BackendConstants.STREAM_MIME_TYPE)
