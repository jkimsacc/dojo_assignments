import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs';

@Injectable()
export class ScoreService {
   user = {};

   constructor(private _http: Http) { }

   retrieveUser(callback) {
      this._http.get('https://api.github.com/jkimsacc').subscribe(
         (response) => {
            this.user = response.json();
            callback(this.user);
         },
         (err) => {
            console.log(err);
         }
      )
   }

}
