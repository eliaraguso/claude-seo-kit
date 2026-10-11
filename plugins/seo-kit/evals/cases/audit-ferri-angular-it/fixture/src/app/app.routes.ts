import { Routes } from '@angular/router';
import { HomeComponent } from './home.component';
import { ChiSiamoComponent } from './chi-siamo.component';
import { ServiziComponent } from './servizi.component';

export const routes: Routes = [
  { path: '', component: HomeComponent, title: 'Studio Ferri Orientamento | Orientamento scolastico a Bologna' },
  { path: 'chi-siamo', component: ChiSiamoComponent, title: 'Chi siamo | Studio Ferri Orientamento' },
  { path: 'servizi', component: ServiziComponent, title: 'Orientamento universitario a Bologna: perchè rivolgersi a uno studio | Studio Ferri' },
  { path: '**', redirectTo: '' },
];
