import { BookMetadata } from "../../data/book.data";
import { Loadable } from "../loadable.data";
import { RestBookMetadataService } from "../rest/interface/book.rest.interface";
import { StoryLordService } from "../story-lord.service";

export class BookService {

    constructor(
        private story_lord: StoryLordService
    ) { }


    async load_book_metadata(): Promise<Loadable<BookMetadata>> {
        if (this.story_lord.book_metadata.is_ok) {
            return this.story_lord.book_metadata;
        }
        if (this.story_lord.book_metadata.loading) {
            return Loadable.from_error<BookMetadata>("Already Loading").with_loading(true);
        }
        await this.story_lord.book_metadata.set(
            this.story_lord.http,
            RestBookMetadataService.load_book_metadata
        )
        return this.story_lord.book_metadata;
    }

    async save_book_metadata() {
        if (this.story_lord.book_metadata.loading) {
            return;
        }
        await this.story_lord.book_metadata.write(
            this.story_lord.http,
            RestBookMetadataService.set_book_metadata
        )
        return this.story_lord.book_metadata;
    }
}