import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ListComponent } from './list/list.component';
import { AddPlayerComponent } from './add-player/add-player.component';
import { GameComponent } from './game/game.component';
import { PlayerComponent } from './player/player.component';
import { GamePlayerComponent } from './game-player/game-player.component';

const routes: Routes = [
   { path: '', pathMatch: 'full', redirectTo: 'player/list'},
   { path: 'player', component: PlayerComponent, children:[
      { path: 'list', pathMatch: 'full', component: ListComponent },
      { path: 'add', component: AddPlayerComponent },
   ]},
   { path: 'game/:id',component: GameComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
