import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { TextEditorComponent } from '../widget/text-editor/text-editor.component';
import { AngularSplitModule } from 'angular-split';
import { FormsModule } from '@angular/forms';
import { StoryLordService } from '../../service/story-lord.service';
import { DropdownSelectorComponent } from '../widget/dropdown-selector/dropdown-selector.component';
import { NgSelectModule, NgSelectConfig } from '@ng-select/ng-select';
import { ChapterContent, ChapterMetaData } from '../../data/chapter.data';
import { IconButtonComponent } from '../widget/shared/icon-button/icon-button.component';
import { result_is_ok } from '../../data/result.data';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    CommonModule,
    TextEditorComponent,
    AngularSplitModule,
    NgSelectModule,
    FormsModule,

    IconButtonComponent,
    DropdownSelectorComponent
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {

  is_loading: boolean = true;
  full_screen: boolean = true;
  primary_active_id: string | null = null;
  secondary_active_id: string | null = null;
  _primary_active_chapter: ChapterContent | null = null;
  _secondary_active_chapter: ChapterContent | null = null;

  constructor(
    public story_service: StoryLordService,
    private config: NgSelectConfig
  ) { }


  ngOnInit() {
    this.setup();
  }

  async setup() {
    this._primary_active_chapter = null;
    this._secondary_active_chapter = null;
    this.update_metadata();
    this.update_chapter_data();
  }

  async update_metadata() {
    await this.story_service.book_sub_service.load_book_metadata();
  }

  async update_chapter_data() {
    this.is_loading = true;
    await this.story_service.chapter_sub_service.get_chapter_metadata();
    this.primary_active_id = this.story_service.chapter_metadata.data?.entities[0].id.string!;
    this.is_loading = false;
    await this.update_primary();
    this.secondary_active_id = this.primary_active_id;
    await this.update_secondary();
  }


  async update_primary() {
    if (this.primary_active_id == null) {
      this._primary_active_chapter = null;
      return;
    }
    if (this.primary_active_id == this.secondary_active_id) {
      this._primary_active_chapter = this._secondary_active_chapter;
    }
    else {
      let response = await this.story_service.chapter_sub_service.get_content_primary(this.primary_active_id);
      if (response.is_errored) {
        // TODO:: Error Handling
        console.log(response.error);
        return
      }
      this._primary_active_chapter = response.data!;
    }
  }

  async update_secondary() {
    if (this.secondary_active_id == null) {
      this._secondary_active_chapter = null;
      return;
    }
    if (this.primary_active_id == this.secondary_active_id) {
      this._secondary_active_chapter = this._primary_active_chapter;
    } else {
      let response = await this.story_service.chapter_sub_service.get_content_primary(this.secondary_active_id);
      if (response.is_errored) {
        // TODO:: Error Handling
        console.log(response.error);
        return
      }
      this._secondary_active_chapter = response.data!;
    }
  }

  get primary_chapter(): ChapterContent | null {
    return this._primary_active_chapter;
  }

  get secondary_chapter(): ChapterContent | null {
    if (this.primary_active_id == this.secondary_active_id) {
      return this._primary_active_chapter;
    }
    return this._secondary_active_chapter;
  }

  toggle(me: HomeComponent) {
    me.full_screen = !me.full_screen;
  }

  async save(me: HomeComponent) {
    if (me._primary_active_chapter != null) {
      let response = await me.story_service.chapter_sub_service.save_content(me._primary_active_chapter);
      if (result_is_ok(response) == false) {
        // TODO: Handle error
        console.log(response.body);
      }
    }
    if (me._secondary_active_chapter != null && me.primary_active_id != me.secondary_active_id) {
      let response = await me.story_service.chapter_sub_service.save_content(me._secondary_active_chapter);
      if (result_is_ok(response) == false) {
        // TODO: Handle error
        console.log(response.body);
      }
    }
  }
}
