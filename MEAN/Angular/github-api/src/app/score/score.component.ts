import { Component, OnInit } from '@angular/core';
import { UserService } from './../user/user.service';

@Component({
  selector: 'app-score',
  templateUrl: './score.component.html',
  styleUrls: ['./score.component.css']
})
export class ScoreComponent implements OnInit {
   user = this._userService;
  constructor(private _userService: UserService) { }

  ngOnInit() {
  }

}
