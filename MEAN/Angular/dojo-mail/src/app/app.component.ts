import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Dojo Mail';
  email: Array<object> = [
    {email: 'bill@gates.com', importance: 'High', subject: "New Windows", content: "Widnows XI will launch in year 2100."},
    {email: 'ada@lovelace.com', importance: 'High', subject: 'Programming', content: 'Enchantress of Numbers'}, 
    {email: 'john@carmac.com', importance: 'Low', subject: 'Updated Algo', content: 'New algorithm for shadow volumnes.'},
    {email: 'gabe@newel.com', importance: 'Low', subject: 'HL3!', content: 'Just kidding...'},  
  ]
}

