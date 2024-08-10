import { HttpClient, HttpHeaders } from "@angular/common/http";
import { RestResult, ResultCode } from "../../data/result.data";
import { firstValueFrom } from "rxjs";
import { Expansion } from "@angular/compiler";
import { ROOT_URL } from "../../app.config";


export class RootRestService {

    static BASE_HEADERS: HttpHeaders | {
        [header: string]: string | string[];
    } = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': 'GET,POST',
            'Access-Control-Allow-Origin': '*' // TODO: repair
        };

    static url(uri: string): string {
        return ROOT_URL + '/' + uri;
    }


    static async get(client: HttpClient, address: string): Promise<RestResult> {
        try {
            return await firstValueFrom(
                client.get<RestResult>(
                    RootRestService.url(address),
                    {
                        headers: RootRestService.BASE_HEADERS
                    }
                )
            );
        } catch (e) {
            console.log(e);
            return {
                code: ResultCode.INTERNAL_ERROR,
                body: (e as Error).toString()
            };
        }
    }


    static async post(client: HttpClient, address: string, data: any): Promise<RestResult> {
        try {
            return await firstValueFrom(
                client.post<RestResult>(
                    RootRestService.url(address),
                    data,
                    {
                        headers: RootRestService.BASE_HEADERS
                    }
                )
            );
        } catch (e) {
            console.log(e);
            return {
                code: ResultCode.INTERNAL_ERROR,
                body: (e as Error).toString()
            };
        }
    }
}
