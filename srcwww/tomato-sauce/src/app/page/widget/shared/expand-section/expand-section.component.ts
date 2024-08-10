import { animate, state, style, transition, trigger } from '@angular/animations';
import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { MatTooltipModule } from '@angular/material/tooltip';

@Component({
  selector: 'tomato-expand-section',
  standalone: true,
  imports: [
    CommonModule,
    MatTooltipModule
  ],
  animations: [
    trigger('expanded', [
      state('opened', style({
        overflow: 'hidden',
        height: '*',
        width: '100%'
      })),
      state('closed', style({
        overflow: 'hidden',
        height: '0px',
        width: '100%'
      })),
      transition('opened => closed', animate('250ms ease-in-out')),
      transition('closed => opened', animate('250ms ease-in-out'))
    ])
  ],
  templateUrl: './expand-section.component.html',
  styleUrl: './expand-section.component.scss'
})
export class ExpandSectionComponent {

  @Input()
  title!: string;

  @Input()
  annotation!: string | null;

  @Input()
  prefix_icon!: string | null;

  state: string = 'closed'

  toggle() {
    this.state = this.state == 'opened' ? 'closed' : 'opened';
  }
}
