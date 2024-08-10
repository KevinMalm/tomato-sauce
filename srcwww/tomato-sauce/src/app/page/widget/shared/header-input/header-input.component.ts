import { Component, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { _String } from '../../../../service/types/string.type';
import { CommonModule } from '@angular/common';
import { MatTooltipModule } from '@angular/material/tooltip';

@Component({
  selector: 'tomato-header-input',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatTooltipModule
  ],
  templateUrl: './header-input.component.html',
  styleUrl: './header-input.component.scss'
})
export class HeaderInputComponent {
  @Input()
  value!: _String;

  @Input()
  prefix_icon: string | null = null;

  @Input()
  annotation: string | null = null;

  @Input()
  placeholder: string = 'Text';
}
