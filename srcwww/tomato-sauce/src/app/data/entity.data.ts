import { _Number } from "../service/types/number.type";
import { _String } from "../service/types/string.type";

export interface Entity {
    id: _String,
    index: _Number,
    name: _String,
    summary: _String,
    aliases: _String[],
    descriptions: _String[],
    relations: _String[]
}

export interface ListEntitiesResponse {
    entities: Entity[]
}

export interface DeleteEntitiesRequestResponse {
    ids: string[]
}