import { HttpClient } from "@angular/common/http";
import { RootRestService } from "../base.rest.interface";
import { firstValueFrom } from "rxjs";
import { ListEntitiesResponse } from "../../../data/entity.data";
import { RestResult } from "../../../data/result.data";

export class RestCharacterService extends RootRestService {
    static LIST_CHARACTER_URL = 'character/list';

    static async load_characters(client: HttpClient): Promise<RestResult> {
        return RootRestService.get(client, this.LIST_CHARACTER_URL);
    }

}
