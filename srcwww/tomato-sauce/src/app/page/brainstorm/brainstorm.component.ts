import { Component } from '@angular/core';
import { ChatRestInterface } from '../../service/rest/interface/chat.rest.interface';
import { HttpClient } from '@angular/common/http';
import { IconButtonComponent } from '../widget/shared/icon-button/icon-button.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { animate, AUTO_STYLE, state, style, transition, trigger } from '@angular/animations';
import { MatTooltipModule } from '@angular/material/tooltip';


const DEFAULT_DURATION = 300;

@Component({
  selector: 'app-brainstorm',
  standalone: true,
  imports: [
    CommonModule,
    IconButtonComponent,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatTooltipModule
  ],
  animations: [
    trigger('collapse', [
      state('false', style({ height: AUTO_STYLE, visibility: AUTO_STYLE })),
      state('true', style({ height: '0', visibility: 'hidden' })),
      transition('false => true', animate(DEFAULT_DURATION + 'ms ease-in')),
      transition('true => false', animate(DEFAULT_DURATION + 'ms ease-out'))
    ])
  ],
  templateUrl: './brainstorm.component.html',
  styleUrl: './brainstorm.component.scss'
})
export class BrainstormComponent {

  prompt: string = '';
  inject_rag: boolean = true;
  expanded_index: number | null = null;
  reference_index: number | null = null;

  constructor(
    public chat_interface: ChatRestInterface,
    private http: HttpClient
  ) { }


  clear(me: BrainstormComponent) {
    me.chat_interface.clear_conversation();
  }

  toggle_rag(me: BrainstormComponent) {
    me.inject_rag = !me.inject_rag;
  }

  toggle_expand(me: BrainstormComponent, index: number) {
    if (this.expanded_index == index) {
      this.expanded_index = null;
      this.reference_index = null;
    } else {
      this.expanded_index = index;
      this.reference_index = Math.floor(index / 2);
    }
  }

  async submit_prompt(me: BrainstormComponent) {
    if (me.prompt.trim().length == 0) {
      return;
    }
    await me.chat_interface.chat(
      me.http,
      me.inject_rag,
      me.prompt
    );
    me.prompt = '';
  }

}
