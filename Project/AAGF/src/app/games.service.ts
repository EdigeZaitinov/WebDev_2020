import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { IGames } from './Games';

@Injectable({
  providedIn: 'root'
})
export class GamesService {

  private games2020url="/assets/games_data/games2020.json"
  private games2019url="/assets/games_data/games2019.json"
  private games2018url="/assets/games_data/games2018.json"
  private games2017url="/assets/games_data/games2017.json"

  constructor(private http:HttpClient) { }
  
  getGames_2020() {
    return this.http.get<IGames[]>(this.games2020url);
  }
  getGames_2019() {
    return this.http.get<IGames[]>(this.games2019url);
  }
  getGames_2018() {
    return this.http.get<IGames[]>(this.games2018url);
  }
  getGames_2017() {
    return this.http.get<IGames[]>(this.games2017url);
  }
}
