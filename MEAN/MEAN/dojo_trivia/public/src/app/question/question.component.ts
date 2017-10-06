import { Component, OnInit } from '@angular/core';
import { Question } from './question'
import { TriviaService } from './../trivia.service'

@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.css']
})
export class QuestionComponent implements OnInit {

   newQuestion = new Question();

   constructor(private _triviaService: TriviaService) { }

   ngOnInit() {
   }

   addQuestion(question: Question){
      console.log("question > addQuestion()" + this.newQuestion)
      this._triviaService.createQuestion(question);
      this.newQuestion = new Question();
   }
}
