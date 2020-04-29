import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersService {
  httpHeader = new HttpHeaders({ "Content-Type": 'application/json' })

  constructor(private http: HttpClient) { }

  getUser(user_email,user_password):Observable<any>{
    return this.http.get('http://127.0.0.1:8000/api/users/'+user_email+'/'+user_password)
  }
}
