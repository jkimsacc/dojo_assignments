import { Injectable } from '@angular/core';

@Injectable()
export class LoginRegistrationService {

   constructor() { }

   login(){
      console.log("service > login()")
   }

   register(user){
      console.log("service > register() " + user.email + user.password)
   }

}
