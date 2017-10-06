import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import 'rxjs';


@Injectable()
export class QuestionService {

   constructor(private _http: Http) { }

   createUser(user) {
      console.log("Service > createUser()" + user)
      return this._http.post('users', user)
      .subscribe(
         (res) => {
            console.log("Service Success");
         },
         (err) => {
            console.log(err)
         }
      )
   }

   retrieveUsers() {
      console.log("Service > retrieveUsers()")
      return this._http.get('/users')
      .map(data => data.json())
      .toPromise();
   }

   createQuestion(question) {
      console.log("Service > createQuestion()" + question)
      return this._http.post('/questions', question)
      .subscribe(
         (res) => {
            console.log("Service Success");
         },
         (err) => {
            console.log(err)
         }
      )
   }

   retrieveQuestions(){
      return this._http.get('/questions')
      .map(data => data.json())
      .toPromise();
   }
   updateScore( score) {
      let header = new Headers();
      header.append('/users', score);
      return this._http.post('/score', score, {headers: header})
      .map(data => data.json())
      .toPromise();
   }
}
