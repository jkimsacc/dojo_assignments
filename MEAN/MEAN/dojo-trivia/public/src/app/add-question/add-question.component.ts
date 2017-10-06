import { Component, OnInit } from '@angular/core';
import { Question } from './../question';
import { Router } from '@angular/router';
import { QuestionService } from './../question.service';


@Component({
  selector: 'app-add-question',
  templateUrl: './add-question.component.html',
  styleUrls: ['./add-question.component.css']
})
export class AddQuestionComponent implements OnInit {
   newQuestion = new Question();

   constructor(
      private _questionService: QuestionService,
      private _router: Router,
   ) { }

   ngOnInit() {
   }

   addQuestion() {
      console.log('add-question.component > addQuestion()')
      this._questionService.createQuestion(this.newQuestion);
      this._router.navigate(['']);
   }

   cancel() {
      console.log('add-question.component > cancel()')
      this._router.navigate(['']);
   }

}
