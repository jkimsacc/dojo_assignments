import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs';

@Injectable()
export class WeatherService {

   constructor(private _http: Http) { }

   retrieveWeather(city: string) {
      return this._http.get('http://api.openweathermap.org/data/2.5/weather?q=${city}&APPID=0b6b441d8f861fc32361cc4b2dbf4c89')
      .map (data => data.json() )
      .toPromise();
   }

}
