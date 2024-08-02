import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'tomato-dropdown-selector',
  standalone: true,
  imports: [
    CommonModule
  ],
  templateUrl: './dropdown-selector.component.html',
  styleUrl: './dropdown-selector.component.scss'
})
export class DropdownSelectorComponent {

  @Input()
  active!: string;

  @Input()
  labels!: string[];

  @Input()
  callback!: Function;

  @Input()
  reference!: any;

}
