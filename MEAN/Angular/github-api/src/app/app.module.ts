import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { UserService } from './user/user.service';
import { AppComponent } from './app.component';
import { UserComponent } from './user/user.component';
import { ScoreComponent } from './score/score.component';

@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    ScoreComponent
  ],
  imports: [
   BrowserModule,
   FormsModule,
	HttpModule,

  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
