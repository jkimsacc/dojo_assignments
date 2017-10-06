import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Swtichboard';
  buttons = [
    { status: "Off"},
    { status: "Off"},
    { status: "Off"},
    { status: "Off"},
    { status: "Off"},
    { status: "Off"},
    { status: "Off"},
    { status: "Off"},
    { status: "Off"},
    { status: "Off"}
]
turn(num){
   if (this.buttons[num].status === 'Off'){
      this.buttons[num].status = "On";
   }
   else{
      this.buttons[num].status = "Off";

   }
}

}
