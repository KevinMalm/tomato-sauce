import { Component, Input } from '@angular/core';
import { AppComponent } from '../../../app.component';
import { AppData } from '../shared/icon-button/app.data';
import { Router } from '@angular/router';
import { IconButtonComponent } from '../shared/icon-button/icon-button.component';
import { StoryLordService } from '../../../service/story-lord.service';
import { Subscription } from 'rxjs';
import { ThinkingState } from '../../../data/thinking.data';
import { CommonModule } from '@angular/common';
import { ProgressSpinnerDirective } from '../../../directive/progress-spinner.directive';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatTooltipModule } from '@angular/material/tooltip';

@Component({
  selector: 'app-drawer',
  standalone: true,
  imports: [
    CommonModule,
    IconButtonComponent,
    MatTooltipModule,

    ProgressSpinnerDirective,
    MatProgressSpinnerModule
  ],
  templateUrl: './app-drawer.component.html',
  styleUrl: './app-drawer.component.scss'
})
export class AppDrawerComponent {

  @Input()
  trigger_callback!: Function;

  @Input()
  app_ref!: AppComponent;


  apps: AppData[] = [
    {
      name: 'Story Board',
      icon: 'story_board',
      url: '/overview'
    },
    {
      name: 'Characters',
      icon: 'people',
      url: '/characters'
    },
    {
      name: 'Locations',
      icon: 'locations',
      url: '/locations'
    },
    {
      name: 'Brain Storming',
      icon: 'brainstorm',
      url: '/brainstorm'
    },
    {
      name: 'Settings',
      icon: 'settings',
      url: '/settings'
    },
  ]

  public thinking_state: ThinkingState = {
    thinking: false,
    message: ''
  }

  private _thinking_subscription!: Subscription;


  constructor(
    private router: Router,
    private story_service: StoryLordService
  ) { }

  check_active(url: string) {
    return url == this.router.url
  }

  navigate(data: any) {
    let me: AppDrawerComponent = data[0];
    let url: string = data[1];

    if (me.check_active(url)) {
      me.trigger_callback(me.app_ref, !me.app_ref.sidebar_open);
    } else {
      me.router.navigate([url]);
      me.trigger_callback(me.app_ref, true);
    }

  }


  ngOnInit() {
    this._thinking_subscription = this.story_service.thinking_state.subscribe(state => this.thinking_state = state);
  }

  ngOnDestroy() {
    this._thinking_subscription.unsubscribe();
  }
}
