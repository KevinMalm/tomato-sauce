import { Component, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { _String } from '../../../../service/types/string.type';
import { MatTooltipModule } from '@angular/material/tooltip';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'tomato-long-input',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatTooltipModule
  ],
  templateUrl: './long-input.component.html',
  styleUrl: './long-input.component.scss'
})
export class LongInputComponent {
  @Input()
  value!: _String;

  @Input()
  prefix_icon: string | null = null;

  @Input()
  annotation: string | null = null;

  @Input()
  placeholder: string = 'Text';
}
