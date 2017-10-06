import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'Retro Barcode';
  colorArray = [];

  createArray() {
     const pool = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];
     for (let i = 0; i < 1000; i++){
        var code = '#';
        for (let j = 0; j < 6; j++){
           code += pool[Math.floor(Math.random() * pool.length)];
        }
        this.colorArray.push(code);
     }
  }
  
  ngOnInit() {
     this.createArray();
  }
}
