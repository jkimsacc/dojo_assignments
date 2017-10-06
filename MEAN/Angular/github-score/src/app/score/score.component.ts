import { Component, OnInit } from '@angular/core';
import { ScoreService } from './score.service';

@Component({
  selector: 'app-score',
  templateUrl: './score.component.html',
  styleUrls: ['./score.component.css']
})
export class ScoreComponent implements OnInit {
   user = { name: "" }
  constructor(private _scoreService: ScoreService) {
     this.getScore();
  }
  getScore(){
     this._scoreService.retrieveUser((user) => {
        this.user = user;
     })
 }

  ngOnInit() {
  }

}
