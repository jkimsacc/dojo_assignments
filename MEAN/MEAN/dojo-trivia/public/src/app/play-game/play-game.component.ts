import { Component, OnInit } from '@angular/core';
import { QuestionService } from './../question.service';
import { Router } from '@angular/router';
import { Question} from './../question';


@Component({
  selector: 'app-play-game',
  templateUrl: './play-game.component.html',
  styleUrls: ['./play-game.component.css']
})
export class PlayGameComponent implements OnInit {
   questions: Array<Question> = [];
   threeQuestions: Array<Question> = [];
   username: String ="";


   constructor(private _questionService: QuestionService, private _router: Router) {
      this.retrieveQuestions();
   }

   ngOnInit() {
   }

   retrieveQuestions() {
      this._questionService.retrieveQuestions()
      .then(questions => {
         this.questions = questions;
         this.pickThree();
      })
   }

   pickThree() {
      for(let i = 0 ; i < 3; i++){
         let randomIdx = Math.floor(Math.random() * this.questions.length)
         this.threeQuestions.push(this.questions[randomIdx]);
         this.questions.splice(randomIdx, 1);
      }
   }

}
