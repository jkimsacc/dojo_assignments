import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent implements OnInit {
   @Output() myEvent = new EventEmitter();

   quote = {
      text: "",
      author: "",
      like: 0,
   }

   addQuote(){
      console.log(this.quote);
      this.myEvent.emit(this.quote);
      this.quote = { text: "", author: "", like: 0 }
   }
  ngOnInit() {
  }

}
