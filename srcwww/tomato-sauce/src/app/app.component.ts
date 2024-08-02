import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { animate, state, style, transition, trigger } from '@angular/animations';
import { AngularSplitModule } from 'angular-split';
import { HomeComponent } from './page/home/home.component';
import { AppDrawerComponent } from './page/widget/app-drawer/app-drawer.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    AngularSplitModule,
    HomeComponent,
    AppDrawerComponent
  ],
  animations: [
    trigger(
      'inOutAnimation',
      [state('open', style({
        width: 'var(--side-bar-max-width)',
        opacity: 1,
      })),
      state('closed', style({
        width: '0px',
        opacity: 1,
      })),
      transition('* => closed', [
        animate('0.5s')
      ]),
      transition('* => open', [
        animate('0.5s')
      ]),]
    )
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'tomato-sauce';

  sidebar_open: boolean = false;

  trigger_sidebar(me: AppComponent, state: boolean) {
    me.sidebar_open = state;
  }

}
