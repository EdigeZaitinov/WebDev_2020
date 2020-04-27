import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders,HttpParams} from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class FilmsService {
  httpHeader=new HttpHeaders({"Content-Type":'application/json'})
  private films_boevik="http://127.0.0.1:8000/api/film_categories/1"
  private films_history="http://127.0.0.1:8000/api/film_categories/2"
  private films_documantal="http://127.0.0.1:8000/api/film_categories/3"
  private films_comedy="http://127.0.0.1:8000/api/film_categories/4"


  constructor(private http:HttpClient) { }

  getFilms_boevik():Observable<any>{
    return this.http.get(this.films_boevik);
    // ,{headers:this.httpHeader})
  }
  getFilms_history():Observable<any>{
    return this.http.get(this.films_history);
    // ,{headers:this.httpHeader})
  }
  getFilms_documantal():Observable<any>{
    return this.http.get(this.films_documantal);
    // ,{headers:this.httpHeader})
  }
  getFilms_comedy():Observable<any>{
    return this.http.get(this.films_comedy);
    // ,{headers:this.httpHeader})
  }
  getFilm(film_name):Observable<any>{
    return this.http.get("http://127.0.0.1:8000/api/film_categories/"+film_name)
  }
}
