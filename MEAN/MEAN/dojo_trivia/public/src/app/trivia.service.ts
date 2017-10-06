import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { User } from './user';
import { Question } from './question/question';
import "rxjs";
import { Observable } from "rxjs";
import { BehaviorSubject } from "rxjs/Rx";

@Injectable()
export class TriviaService {
   currentUser = ""
   users:Array<User> = [];
   userObserver = new BehaviorSubject(this.users)
   questions = [];

   constructor(private _http: Http) { }

   createUser(user: User) {
      console.log("service > create user")
      return this._http.post('/users', user)
      .map(data => data.json()).toPromise()
   }

   getUsers(callback){
      this._http.get('/users').subscribe(
         (res) =>{
            this.users = res.json();
            callback(this.users);
         },
         (err) => {
            console.log(err)
         },
      )
   }

   createQuestion(question: Question){
      console.log("service > createQuestion", question)
      return this._http.post('/questions', question)
      .map(data => data.json()).toPromise()
   }
}
