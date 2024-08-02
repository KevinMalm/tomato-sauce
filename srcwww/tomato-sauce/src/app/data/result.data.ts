
export class ResultCode {
    static OK = 200
    static PROMPT_ERROR = 340
    static INTERNAL_ERROR = 350
}

export interface RestError {
    header: string,
    message: string
}

export interface RestResult {
    body: any
    code: number

}

export function result_is_ok(result: RestResult): boolean {
    return result.code == ResultCode.OK
}
