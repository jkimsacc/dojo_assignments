import { Component, OnInit } from '@angular/core';
import { PlayerService } from './../player.service';


@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {
   players = [];

   constructor(private _playerService: PlayerService) {

   }
   ngOnInit(){
      this.getPlayers();
   }

   getPlayers(){
      this._playerService.playerObserver.subscribe(
         (players) => this.players = players,
         (err) => console.log(err)
      )
   }

   delete(player){
      console.log("list > delete(player)")
      this._playerService.delete(player)
   }


}
