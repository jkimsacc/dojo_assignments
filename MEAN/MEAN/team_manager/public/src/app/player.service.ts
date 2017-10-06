import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { Player } from './player'
import "rxjs";
import { Observable } from "rxjs";
import { BehaviorSubject} from "rxjs/Rx";

@Injectable()
export class PlayerService {
   players:Array<Player> =[];
   playerObserver = new BehaviorSubject(this.players)

   constructor(private _http: Http) { }

   createPlayer(player: Player){
      console.log("service > createPlayer()");
      return this._http.post('/players', player)
      .map(data => data.json()).toPromise()
   }

   getPlayers() {
      return this._http.get('/players')
      .subscribe(
         (res) =>{
            this.players = res.json();
            this.playerObserver.next(this.players)
         },
         (err) => {
            console.log(err)
         },
      )
   }

   updateStatus(player: Player, game: String, status: String){
      console.log("service > updateStatus()")
      this._http.put("players/" + player._id,{
         game: game,
         status: status
      })
      .map(data => data.json()).toPromise()
   }

   delete(player){
      console.log("service > delete(player)")
      return this._http.delete("/players/"+player._id, player)
      .map(data => data.json()).toPromise()
   }
}
