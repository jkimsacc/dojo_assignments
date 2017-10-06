import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {
   @Input() quoteList;
   @Output() vote = new EventEmitter();
   @Output() down = new EventEmitter();
   @Output() del = new EventEmitter();

   upVote(quote){
      this.vote.emit(quote)
   }
   downVote(quote){
      this.down.emit(quote)
   }
   delete(quote){
      this.del.emit(quote);
   }

  constructor() { }

  ngOnInit() {
  }

}
