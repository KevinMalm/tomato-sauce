import { Component, Input } from '@angular/core';
import { AppComponent } from '../../../app.component';
import { AppData } from '../shared/icon-button/app.data';
import { Router } from '@angular/router';
import { IconButtonComponent } from '../shared/icon-button/icon-button.component';

@Component({
  selector: 'app-drawer',
  standalone: true,
  imports: [
    IconButtonComponent
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


  constructor(
    private router: Router
  ) { }

  check_active(url: string) {
    return url == this.router.url
  }

  navigate(data: any) {
    let me: AppDrawerComponent = data[0];
    let url: string = data[1];

    if (me.check_active(url)) {
      me.trigger_callback(me.app_ref, me.app_ref.sidebar_open);
    } else {
      me.router.navigate([url]);
      me.trigger_callback(me.app_ref, true);
    }

  }

}
