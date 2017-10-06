import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { User } from './user';
import 'rxjs';
@Injectable()
export class UserService {
   username = User.name;
   constructor(private _http: Http) { }
   retrieveUser(callback) {
      this._http.get('https://api.github.com/users/' + this.username).subscribe(
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
