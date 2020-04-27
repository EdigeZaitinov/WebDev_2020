import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders,HttpParams} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GamesService {
  httpHeader=new HttpHeaders({"Content-Type":'application/json'})
  private games2020url="http://127.0.0.1:8000/api/game_categories/4"
  private games2019url="http://127.0.0.1:8000/api/game_categories/3"
  private games2018url="http://127.0.0.1:8000/api/game_categories/2"
  private games2017url="http://127.0.0.1:8000/api/game_categories/1"

  constructor(private http:HttpClient) { }
  
  getGames_2020():Observable<any>{
    return this.http.get(this.games2020url);
    // ,{headers:this.httpHeader})
  }
  getGames_2019():Observable<any>{
    return this.http.get(this.games2019url);
    // ,{headers:this.httpHeader})
  }
  getGames_2018():Observable<any>{
    return this.http.get(this.games2018url);
    // ,{headers:this.httpHeader})
  }
  getGames_2017():Observable<any>{
    return this.http.get(this.games2017url);
    // ,{headers:this.httpHeader})
  }
  getGame(game_name):Observable<any>{
    return this.http.get("http://127.0.0.1:8000/api/game_categories/"+game_name)
  }
}
