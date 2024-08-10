import { HttpClient } from "@angular/common/http";
import { RootRestService } from "../base.rest.interface";
import { RestResult } from "../../../data/result.data";
import { _String } from "../../types/string.type";
import { AddChapterRequest, ChapterContent } from "../../../data/chapter.data";
import { RestCharacterService } from "./character.rest.interface";

export class RestChapterMetadataService extends RootRestService {
    static LIST_CHAPTER_METADATA_URL = 'chapters/metadata';
    static ADD_CHAPTER_METADATA_URL = 'chapters/add';
    static CHAPTER_CONTENT_URL = 'chapters/content?id=';

    static async load_chapter_metadata(client: HttpClient): Promise<RestResult> {
        return RootRestService.get(client, RestChapterMetadataService.LIST_CHAPTER_METADATA_URL);
    }

    static async load_chapter_content(client: HttpClient, id: string): Promise<RestResult> {
        return RootRestService.get(client, RestChapterMetadataService.CHAPTER_CONTENT_URL + id);
    }

    static async add_chapter(client: HttpClient, request: AddChapterRequest): Promise<RestResult> {
        return RootRestService.post(client, RestChapterMetadataService.ADD_CHAPTER_METADATA_URL, request);
    }

    static async save_chapter_content(client: HttpClient, content: ChapterContent): Promise<RestResult> {
        return RootRestService.post(client, RestChapterMetadataService.CHAPTER_CONTENT_URL, content);
    }

}
