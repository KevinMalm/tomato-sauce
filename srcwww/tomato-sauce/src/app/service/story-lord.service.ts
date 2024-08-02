import { Injectable } from '@angular/core';
import { Loadable } from './loadable.data';
import { ChapterContent, ListChapterMetadataResponse } from '../data/chapter.data';
import { ListEntitiesResponse } from '../data/entity.data';
import { HttpClient } from '@angular/common/http';
import { RestChapterMetadataService } from './rest/interface/chapter.rest.interface';
import { RestResult, result_is_ok } from '../data/result.data';

@Injectable({
  providedIn: 'root'
})
export class StoryLordService {

  chapter_metadata: Loadable<ListChapterMetadataResponse> = new Loadable();
  characters: Loadable<ListEntitiesResponse> = new Loadable();
  locations: Loadable<ListEntitiesResponse> = new Loadable();

  chapter_primary: Loadable<ChapterContent> = new Loadable();
  chapter_secondary: Loadable<ChapterContent> = new Loadable();

  constructor(
    private http: HttpClient
  ) { }


  async get_chapter_metadata(): Promise<Loadable<ListChapterMetadataResponse>> {
    if (this.chapter_metadata.is_loaded) {
      return this.chapter_metadata;
    }
    if (this.chapter_metadata.loading) {
      return Loadable.from_error<ListChapterMetadataResponse>("Already Loading").with_loading(true);
    }
    await this.chapter_metadata.set(
      this.http,
      RestChapterMetadataService.load_chapter_metadata
    );
    return this.chapter_metadata;
  }

  async get_content_primary(id: string): Promise<Loadable<ChapterContent>> {
    if (this.chapter_primary.is_loaded && this.chapter_primary.data!.id.string == id) {
      return this.chapter_primary;
    }
    this.chapter_primary._clear();
    let response = await RestChapterMetadataService.load_chapter_content(this.http, id);
    if (result_is_ok(response)) {
      this.chapter_primary.data = (response.body as ChapterContent)
    } else {
      this.chapter_primary.error = (response.body as string)
    }
    return this.chapter_primary;
  }

  async get_content_secondary(id: string): Promise<Loadable<ChapterContent>> {
    if (this.chapter_secondary.is_loaded && this.chapter_secondary.data!.id.string == id) {
      return this.chapter_primary;
    }
    this.chapter_secondary._clear();
    let response = await RestChapterMetadataService.load_chapter_content(this.http, id);
    if (result_is_ok(response)) {
      this.chapter_secondary.data = (response.body as ChapterContent)
    } else {
      this.chapter_secondary.error = (response.body as string)
    }
    return this.chapter_secondary;
  }

  async save_content(content: ChapterContent): Promise<RestResult> {
    let response = await RestChapterMetadataService.save_chapter_content(this.http, content);
    return response;
  }
}
