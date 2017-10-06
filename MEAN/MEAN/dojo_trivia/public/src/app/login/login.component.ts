import { Component, OnInit } from '@angular/core';
import { TriviaService } from './../trivia.service';
import { User } from './../user';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
   users:Array<User> = [];
   newUser = new User;
   loggedIn = false;

   constructor(private _triviaService: TriviaService) {
      this.getUsers();
      }
      getUsers() {
         this._triviaService.getUsers((users) => {
            console.log(users);
            this.users = users;
         })
      }

   ngOnInit() { }

   login(user: User){
      console.log("Component > login()", this.newUser)
      this._triviaService.createUser(user);
      this.newUser = new User();
      this.loggedIn = true;
   }
}
