import { Injectable } from '@angular/core';
import { Loadable } from './loadable.data';
import { ChapterContent, ListChapterMetadataResponse } from '../data/chapter.data';
import { ListEntitiesResponse } from '../data/entity.data';
import { HttpClient } from '@angular/common/http';
import { RestChapterMetadataService } from './rest/interface/chapter.rest.interface';
import { RestResult, result_is_ok } from '../data/result.data';
import { Socket } from 'ngx-socket-io';
import { ThinkingState } from '../data/thinking.data';
import { BookMetadata } from '../data/book.data';
import { RestBookMetadataService } from './rest/interface/book.rest.interface';
import { _String } from './types/string.type';
import * as uuid from 'uuid';
import { BookService } from './subservice/book.service';
import { ChapterService } from './subservice/chapter.service';

@Injectable({
  providedIn: 'root'
})
export class StoryLordService {
  static THINKING_SOCKET_TAG = 'thinking';

  thinking_state = this.socket.fromEvent<ThinkingState>(StoryLordService.THINKING_SOCKET_TAG);

  book_metadata: Loadable<BookMetadata> = new Loadable();
  chapter_metadata: Loadable<ListChapterMetadataResponse> = new Loadable();
  characters: Loadable<ListEntitiesResponse> = new Loadable();
  locations: Loadable<ListEntitiesResponse> = new Loadable();

  chapter_primary: Loadable<ChapterContent> = new Loadable();
  chapter_secondary: Loadable<ChapterContent> = new Loadable();


  public book_sub_service = new BookService(this);
  public chapter_sub_service = new ChapterService(this);

  constructor(
    public http: HttpClient,
    private socket: Socket
  ) { }

  static uuid(): _String {
    return {
      string: uuid.v4()
    }
  }
}
