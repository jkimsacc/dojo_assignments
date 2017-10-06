import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login-registration',
  templateUrl: './login-registration.component.html',
  styleUrls: ['./login-registration.component.css']
})
export class LoginRegistrationComponent implements OnInit {
   login_tab = true

   constructor() { }

   ngOnInit() {
   }

   registerTab(){
      this.login_tab = false;
   }
   loginTab(){
      this.login_tab = true;
   }

}
