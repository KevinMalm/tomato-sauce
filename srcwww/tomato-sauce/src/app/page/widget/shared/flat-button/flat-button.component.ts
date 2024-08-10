import { Component, Input } from '@angular/core';
import { ButtonDirection } from '../icon-button/icon-button.component';
import { CommonModule } from '@angular/common';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { ProgressSpinnerDirective } from '../../../../directive/progress-spinner.directive';

@Component({
  selector: 'tomato-flat-button',
  standalone: true,
  imports: [
    CommonModule,

    ProgressSpinnerDirective,
    MatProgressSpinnerModule,
    MatTooltipModule
  ],
  templateUrl: './flat-button.component.html',
  styleUrl: './flat-button.component.scss'
})
export class FlatButtonComponent {
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
  loading: boolean = false;

  @Input()
  direction: ButtonDirection = 'horizontal';
}
