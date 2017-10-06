import { Component, OnInit } from '@angular/core';
import { WeatherService } from './../weather.service';


@Component({
  selector: 'app-washingtondc',
  templateUrl: './washingtondc.component.html',
  styleUrls: ['./washingtondc.component.css']
})
export class WashingtondcComponent implements OnInit {
   weather;
   humidity;
   temp;
   temp_max;
   temp_min;
   constructor(private _weatherService: WeatherService) { }

   ngOnInit() {
      this.weather = this._weatherService.retrieveWeather('4140963')
      .then( weather => {
         this.humidity = weather.main.humidity;
         this.temp = weather.main.temp;
         this.temp_max = weather.main.temp_max;
         this.temp_min = weather.main.temp_min;
      });

   }

}
