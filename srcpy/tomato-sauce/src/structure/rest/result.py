from dataclasses import dataclass
from shared.util import to_json


class ResultCode:
    OK = 200
    PROMPT_ERROR = 340
    INTERNAL_ERROR = 350


@dataclass
class RestResult:

    @dataclass
    class Error:
        header: str
        message: str

    body: dataclass
    code: int

    @staticmethod
    def ok(body: dataclass):
        return to_json(RestResult(body, ResultCode.OK))

    @staticmethod
    def prompt_error(header: str, message: str):
        return to_json(
            RestResult(RestResult.Error(header, message), ResultCode.PROMPT_ERROR)
        )

    @staticmethod
    def internal_error(source: str, message: str):
        return to_json(
            RestResult(RestResult.Error(source, message), ResultCode.INTERNAL_ERROR)
        )
