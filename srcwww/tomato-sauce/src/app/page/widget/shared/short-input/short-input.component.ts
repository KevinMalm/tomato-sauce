import { Component, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { _String } from '../../../../service/types/string.type';

@Component({
  selector: 'tomato-short-input',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './short-input.component.html',
  styleUrl: './short-input.component.scss'
})
export class ShortInputComponent {
  @Input()
  value!: _String;

  @Input()
  placeholder: string = 'Text';
}
