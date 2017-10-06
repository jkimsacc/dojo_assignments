import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LeaderBoardComponent } from './leader-board/leader-board.component';
import { AddQuestionComponent } from './add-question/add-question.component';
import { PlayGameComponent } from './play-game/play-game.component';

const routes: Routes = [
   { path: '', pathMatch:'full', component: LeaderBoardComponent },
   { path: 'new_question', pathMatch: 'full', component: AddQuestionComponent },
   { path: 'play', pathMatch: 'full', component: PlayGameComponent },
   { path: 'logout', pathMatch: 'full', component: LeaderBoardComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
