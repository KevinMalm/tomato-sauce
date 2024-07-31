import { Routes } from '@angular/router';
import { ErrorComponent } from './page/widget/error/error.component';
import { OverviewComponent } from './page/overview/overview.component';
import { CharacterComponent } from './page/character/character.component';
import { LocalCharacterComponent } from './page/character/local-character/local-character.component';
import { LocationComponent } from './page/location/location.component';
import { LocalLocationComponent } from './page/location/local-location/local-location.component';
import { BrainstormComponent } from './page/brainstorm/brainstorm.component';
import { SettingsComponent } from './page/settings/settings.component';

export const routes: Routes = [
    { path: '', component: ErrorComponent },
    { path: 'overview', component: OverviewComponent },
    { path: 'characters', component: CharacterComponent },
    { path: 'characters/:id', component: LocalCharacterComponent },
    { path: 'locations', component: LocationComponent },
    { path: 'locations/:id', component: LocalLocationComponent },
    { path: 'brainstorm', component: BrainstormComponent },
    { path: 'settings', component: SettingsComponent },
];
