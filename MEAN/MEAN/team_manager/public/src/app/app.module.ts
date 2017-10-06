import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { PlayerService } from './player.service';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ListComponent } from './list/list.component';
import { AddPlayerComponent } from './add-player/add-player.component';
import { GameComponent } from './game/game.component';
import { PlayerComponent } from './player/player.component';
import { GamePlayerComponent } from './game-player/game-player.component';

@NgModule({
  declarations: [
    AppComponent,
    ListComponent,
    AddPlayerComponent,
    GameComponent,
    PlayerComponent,
    GamePlayerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule,

  ],
  providers: [PlayerService],
  bootstrap: [AppComponent]
})
export class AppModule { }
