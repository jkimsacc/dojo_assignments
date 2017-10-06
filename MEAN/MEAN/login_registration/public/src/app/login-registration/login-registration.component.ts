import { Component, OnInit } from '@angular/core';
import { LoginRegistrationService } from './../login-registration.service';

import { User } from './../user';

@Component({
  selector: 'app-login-registration',
  templateUrl: './login-registration.component.html',
  styleUrls: ['./login-registration.component.css']
})
export class LoginRegistrationComponent implements OnInit {
   login_page = true;
   newUser = new User();

   constructor(private _login_registrationService: LoginRegistrationService) { }

   ngOnInit() {
   }

   registerPage(){
      this.login_page = false;
   }

   loginPage(){
      this.login_page = true;
   }

   login(){
      console.log("login > login()", this.newUser)
      this._login_registrationService.login();
   }

   register(){
      console.log("register > register()", this.newUser);
      this._login_registrationService.register(this.newUser);
   }

}
