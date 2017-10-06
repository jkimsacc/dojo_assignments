import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Registration';
  states = ['WA', 'OR', 'CA', 'AL', 'ETC'];
  users = [];
  user = {
     first_name: '',
     last_name: '',
     email: '',
     password: '',
     address_st: '',
     address_unit: '',
     city: '',
     state: '',
     feeling: '',
  }
  register(){
     console.log('register');
     this.users.push(this.user);
 }
}
