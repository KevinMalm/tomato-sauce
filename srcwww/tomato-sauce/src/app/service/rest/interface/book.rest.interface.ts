import { HttpClient } from "@angular/common/http";
import { RootRestService } from "../base.rest.interface";
import { RestResult } from "../../../data/result.data";
import { _String } from "../../types/string.type";
import { ChapterContent } from "../../../data/chapter.data";
import { BookMetadata } from "../../../data/book.data";

export class RestBookMetadataService extends RootRestService {
    static BOOK_METADATA_URL = 'book/metadata';

    static async load_book_metadata(client: HttpClient): Promise<RestResult> {
        return RootRestService.get(client, RestBookMetadataService.BOOK_METADATA_URL);
    }

    static async set_book_metadata(client: HttpClient, data: BookMetadata): Promise<RestResult> {
        return RootRestService.post(client, RestBookMetadataService.BOOK_METADATA_URL, data);
    }

}
