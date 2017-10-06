import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginRegistrationComponent } from './login-registration/login-registration.component';
import { CreateEventComponent } from './create-event/create-event.component';

const routes: Routes = [
   { path: '', pathMatch: "full", component: LoginRegistrationComponent },
   { path: 'create', pathMatch: "full", component: CreateEventComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
