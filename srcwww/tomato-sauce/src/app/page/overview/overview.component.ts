import { Component } from '@angular/core';
import { StoryLordService } from '../../service/story-lord.service';
import { CommonModule } from '@angular/common';
import { HeaderInputComponent } from '../widget/shared/header-input/header-input.component';
import { ExpandSectionComponent } from '../widget/shared/expand-section/expand-section.component';
import { DropdownSelectorComponent } from "../widget/dropdown-selector/dropdown-selector.component";
import { LongInputComponent } from '../widget/shared/long-input/long-input.component';
import { CdkDragDrop, DragDropModule, moveItemInArray } from '@angular/cdk/drag-drop';
import { ShortInputComponent } from "../widget/shared/short-input/short-input.component";
import { _String } from '../../service/types/string.type';
import { FlatButtonComponent } from '../widget/shared/flat-button/flat-button.component';
import { IconButtonComponent } from '../widget/shared/icon-button/icon-button.component';

@Component({
  selector: 'app-overview',
  standalone: true,
  imports: [
    CommonModule,
    HeaderInputComponent,
    ExpandSectionComponent,
    LongInputComponent,
    DropdownSelectorComponent,
    DragDropModule,
    FlatButtonComponent,
    IconButtonComponent,
    ShortInputComponent
  ],
  templateUrl: './overview.component.html',
  styleUrl: './overview.component.scss'
})
export class OverviewComponent {

  new_chapter_prompt = 'New Chapter';
  chapter_input_name: _String = {
    string: ''
  }
  loading_new_chapter: boolean = false;

  constructor(
    public story_service: StoryLordService
  ) { }


  ngOnInit() {
    this.update_metadata();
  }

  async update_metadata() {
    await this.story_service.book_sub_service.load_book_metadata();
    await this.story_service.chapter_sub_service.get_chapter_metadata();
  }

  drop(event: CdkDragDrop<string[]>) {
    moveItemInArray(this.story_service.chapter_metadata.data!.entities, event.previousIndex, event.currentIndex);
  }

  async add_new_chapter(me: OverviewComponent) {
    if (me.chapter_input_name.string.length == 0) {
      me.new_chapter_prompt = 'REQUIRED: New Chapter Name'
      return;
    }
    me.new_chapter_prompt = 'New Chapter';
    me.loading_new_chapter = true;
    me.story_service.chapter_metadata.data!.entities.push({
      id: StoryLordService.uuid(),
      title: {
        string: me.chapter_input_name.string
      },
      index: {
        number: me.story_service.chapter_metadata.data!.entities.length
      },
      involved_characters: [],
      involved_locations: []
    })
    await me.story_service.chapter_sub_service.add_chapter({
      id: StoryLordService.uuid(),
      title: {
        string: me.chapter_input_name.string
      },
      index: {
        number: me.story_service.chapter_metadata.data!.entities.length
      },
      summary: {
        string: ''
      }
    })
    this.loading_new_chapter = false;
    me.chapter_input_name.string = '';
  }

  async save_book_metadata(me: OverviewComponent) {
    await me.story_service.book_sub_service.save_book_metadata();
    me.chapter_input_name.string = '';
  }

  get book_summary_formatted(): string {
    let summary = this.story_service.book_metadata.data?.summary?.string;
    if (summary == null || summary.length == 0) {
      return 'Once upon a time...';
    }
    return summary
  }
}


