import { Component, Input } from '@angular/core';
import { ChapterContent } from '../../../data/chapter.data';
import { QuillModule } from 'ngx-quill';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

import Quill from 'quill';
import { _String } from '../../../service/types/string.type';

@Component({
  selector: 'app-text-editor',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    QuillModule,
  ],
  templateUrl: './text-editor.component.html',
  styleUrl: './text-editor.component.scss'
})
export class TextEditorComponent {
  private quillEditor!: Quill;

  @Input()
  content!: _String;

}
