import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  quotes = [];

   sort(arr, index=arr.length-1){
      if (index === 0){
        return arr;
      }
      else if (arr[index].like > arr[index-1].like){
        let temp = arr[index];
        arr[index] = arr[index-1];
        arr[index-1] = temp;
        this.sort(arr, arr.length-1);
      }
      this.sort(arr, index-1)
   }


   pushQuote(event){
     this.quotes.push(event);
     this.sort(this.quotes, this.quotes.length-1)
   }
   upVote(event){
      event.like += 1;
      this.sort(this.quotes, this.quotes.length-1)
   }
   downVote(event){
      event.like -= 1;
      this.sort(this.quotes, this.quotes.length-1)
   }
   delete(event){
      for (let i = 0; i < this.quotes.length; i++){
         if (this.quotes[i] === event){
            this.quotes[i] = this.quotes[i+1];
         }
      }
      this.quotes.length --;
   }
}
