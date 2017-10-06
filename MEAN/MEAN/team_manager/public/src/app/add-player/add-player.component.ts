import { Component, OnInit } from '@angular/core';
import { PlayerService } from './../player.service';
import { Player } from './../player'

@Component({
  selector: 'app-add-player',
  templateUrl: './add-player.component.html',
  styleUrls: ['./add-player.component.css']
})

export class AddPlayerComponent implements OnInit {
   newPlayer = new Player();
   players = [];

   constructor(private _playerService: PlayerService) { }

   ngOnInit() {
   }

   addPlayer(player: Player){
      console.log("add-player > addPlayer()")
      this._playerService.createPlayer(this.newPlayer);
      this.newPlayer = new Player();
      this.players = this._playerService.players;
   }

}
