import { _Number } from "../service/types/number.type";
import { _String } from "../service/types/string.type";
import { Entity } from "./entity.data";

export interface AddChapterRequest {
    id: _String,
    title: _String,
    index: _Number,
    summary: _String
}

export interface ChapterMetaData {
    id: _String,
    title: _String,
    index: _Number,
    involved_characters: Entity[],
    involved_locations: Entity[],
}

export interface ListChapterMetadataResponse {
    entities: ChapterMetaData[]
}

export interface ChapterContent {
    id: _String,
    content: _String
}