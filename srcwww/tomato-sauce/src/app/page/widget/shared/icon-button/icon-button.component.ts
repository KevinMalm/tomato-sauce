import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { MatTooltipModule } from '@angular/material/tooltip';

export type ButtonDirection = 'horizontal' | 'vertical';


@Component({
  selector: 'tomato-icon-button',
  standalone: true,
  imports: [
    CommonModule,
    MatTooltipModule
  ],
  templateUrl: './icon-button.component.html',
  styleUrl: './icon-button.component.scss'
})
export class IconButtonComponent {

  @Input()
  callback!: Function;

  @Input()
  callback_args!: any;

  @Input()
  icon_path!: string;

  @Input()
  label: string | null = null;

  @Input()
  active!: boolean;

  @Input()
  direction: ButtonDirection = 'horizontal';

}
