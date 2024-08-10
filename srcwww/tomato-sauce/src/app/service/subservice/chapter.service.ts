import { ListChapterMetadataResponse, ChapterContent, AddChapterRequest } from "../../data/chapter.data";
import { result_is_ok, RestResult } from "../../data/result.data";
import { Loadable } from "../loadable.data";
import { RestChapterMetadataService } from "../rest/interface/chapter.rest.interface";
import { StoryLordService } from "../story-lord.service";


export class ChapterService {

    constructor(
        private story_lord: StoryLordService
    ) { }

    async add_chapter(details: AddChapterRequest): Promise<Loadable<ListChapterMetadataResponse>> {
        if (this.story_lord.chapter_metadata.loading) {
            return Loadable.from_error<ListChapterMetadataResponse>("Already Loading").with_loading(true);
        }

        this.story_lord.chapter_metadata._clear();
        let response = await RestChapterMetadataService.add_chapter(this.story_lord.http, details);
        if (result_is_ok(response)) {
            this.story_lord.chapter_metadata.data = (response.body as ListChapterMetadataResponse);
        } else {
            this.story_lord.chapter_metadata.error = (response.body as string);
        }
        this.story_lord.chapter_metadata.loading = false;
        return this.story_lord.chapter_metadata;
    }

    async get_chapter_metadata(): Promise<Loadable<ListChapterMetadataResponse>> {
        if (this.story_lord.chapter_metadata.is_ok) {
            return this.story_lord.chapter_metadata;
        }
        if (this.story_lord.chapter_metadata.loading) {
            return Loadable.from_error<ListChapterMetadataResponse>("Already Loading").with_loading(true);
        }
        console.log("Refreshing Chapter Metadata...")
        await this.story_lord.chapter_metadata.set(
            this.story_lord.http,
            RestChapterMetadataService.load_chapter_metadata
        );
        return this.story_lord.chapter_metadata;
    }

    async get_content_primary(id: string): Promise<Loadable<ChapterContent>> {
        if (this.story_lord.chapter_primary.is_ok && this.story_lord.chapter_primary.data!.id.string == id) {
            return this.story_lord.chapter_primary;
        }
        this.story_lord.chapter_primary._clear();
        let response = await RestChapterMetadataService.load_chapter_content(this.story_lord.http, id);
        if (result_is_ok(response)) {
            this.story_lord.chapter_primary.data = (response.body as ChapterContent)
        } else {
            this.story_lord.chapter_primary.error = (response.body as string)
        }
        return this.story_lord.chapter_primary;
    }

    async get_content_secondary(id: string): Promise<Loadable<ChapterContent>> {
        if (this.story_lord.chapter_secondary.is_ok && this.story_lord.chapter_secondary.data!.id.string == id) {
            return this.story_lord.chapter_primary;
        }
        this.story_lord.chapter_secondary._clear();
        let response = await RestChapterMetadataService.load_chapter_content(this.story_lord.http, id);
        if (result_is_ok(response)) {
            this.story_lord.chapter_secondary.data = (response.body as ChapterContent)
        } else {
            this.story_lord.chapter_secondary.error = (response.body as string)
        }
        return this.story_lord.chapter_secondary;
    }

    async save_content(content: ChapterContent): Promise<RestResult> {
        let response = await RestChapterMetadataService.save_chapter_content(this.story_lord.http, content);
        return response;
    }
}