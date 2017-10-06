import { Component, OnInit } from '@angular/core';
import { PlayerService } from './../player.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {

   players = [];
   game_num = "1";
   game = "game1";

   constructor(private _route: ActivatedRoute, private _playerService: PlayerService ) { }

   ngOnInit() {
      this._playerService.playerObserver.subscribe(players => {
         this.players = players;
      });
      this.getPlayers();
   }

   getPlayers(){
      console.log("game > getPlayers()")
      this._playerService.playerObserver.subscribe(
         (players) => this.players = players,
         (err) => console.log(err)
      )
   }

   updateStatus(player, status){
      console.log("game > updateStatus()")
      this._playerService.updateStatus(
         player, this.game, status)
      .then(status => this.getPlayers())
   }
}
