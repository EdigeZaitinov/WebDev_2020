import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {RouterModule,Routes, Router} from '@angular/router';
import {HttpClientModule, HttpClient} from '@angular/common/http';
import {FormsModule} from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { SiteComponent } from './site/site.component';
import { FilmsComponent } from './site/films/films.component';
import { GamesComponent } from './site/games/games.component';
import { AboutUsComponent } from './site/about-us/about-us.component';
import { GamesService } from './games.service';
import { GameComponent } from './site/games/game/game.component';
import { FilmComponent } from './site/films/film/film.component';

const appRoutes:Routes=[
  {path:'',component:LoginComponent},
  {path:'AAGF',component:SiteComponent},
  {path:'AAGF/games',component:GamesComponent},
  {path:'AAGF/games/:gameName',component:GameComponent},
  {path:'AAGF/films',component:FilmsComponent},
  {path:'AAGF/films/:filmName',component:FilmComponent},
  {path:'AAGF/about_us',component:AboutUsComponent}
]

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SiteComponent,
    FilmsComponent,
    GamesComponent,
    AboutUsComponent,
    GameComponent,
    FilmComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
    FormsModule
  ],
  providers: [GamesService],
  bootstrap: [AppComponent]
})
export class AppModule { }
