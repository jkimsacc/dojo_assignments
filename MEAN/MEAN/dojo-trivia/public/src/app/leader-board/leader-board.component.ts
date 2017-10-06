import { Component, OnInit } from '@angular/core';
import { QuestionService } from './../question.service';
import { Router } from '@angular/router';
import { User } from './../user';

@Component({
  selector: 'app-leader-board',
  templateUrl: './leader-board.component.html',
  styleUrls: ['./leader-board.component.css']
})
export class LeaderBoardComponent implements OnInit {
   user = new User();
   users: Array<User> = [];


   constructor(private _questionService: QuestionService, private _router: Router) {
      this.retrieveUsers();
   }

   ngOnInit() {
      this.createUser();
   }

   createUser() {
      let username = prompt("Input username");
      this.user.username = username;
      if(username) {
         console.log("leader-board.Component > createUser()" + this.user.username)
         this._questionService.createUser(this.user);
      }
   }

   retrieveUsers(){
      console.log("leader-board > retrieveUsers");
      this._questionService.retrieveUsers()
      .then(users => {
         this.users = users;
      })
   }

   // getUsers(){
   //
   // }

}
