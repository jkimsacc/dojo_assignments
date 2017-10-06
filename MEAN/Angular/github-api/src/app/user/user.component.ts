import { Component, OnInit } from '@angular/core';
import { UserService } from './user.service';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {
   user: { User };

  constructor(private _userService: UserService) {
     this.retrieveUser();
  }
  retrieveUser(){
   this._userService.retrieveUser((username) => {
      this.user = username;
      });
   }

   ngOnInit() {

   }

}
