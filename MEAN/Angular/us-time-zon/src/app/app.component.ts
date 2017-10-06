import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'US Time Zone';
  now;
  lastClicked;

  setTimezone(timezone){
     this.now = new Date();
     if (timezone == 'pct'){
        this.now = new Date();
     }
     if (timezone == 'mst'){
        this.now.setHours(this.now.getHours() +1 );
     }
     if (timezone == 'cst'){
       this.now.setHours(this.now.getHours() + 2 );

     }
     if (timezone == 'est'){
        this.now.setHours(this.now.getHours() + 3 );
     }
     if (timezone == 'clear'){
        this.now = null;
     }
     this.lastClicked = timezone;
  }
}
