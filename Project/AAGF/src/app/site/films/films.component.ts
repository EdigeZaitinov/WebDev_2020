import { Component, OnInit } from '@angular/core';
import { FilmsService } from 'src/app/films.service';

@Component({
  selector: 'app-films',
  templateUrl: './films.component.html',
  styleUrls: ['./films.component.css']
})
export class FilmsComponent implements OnInit {
  filmsall=[]

  constructor(private film_service:FilmsService) { }

  ngOnInit(): void {
    this.film_service.getFilms_boevik().subscribe(data=>this.filmsall=data)
  }

  btn_films_boevik(){
    this.film_service.getFilms_boevik().subscribe(data=>this.filmsall=data)
  }
  btn_films_history(){
    this.film_service.getFilms_history().subscribe(data=>this.filmsall=data)
  }
  btn_films_documental(){
    this.film_service.getFilms_documantal().subscribe(data=>this.filmsall=data)
  }
  btn_films_comedy(){
    this.film_service.getFilms_comedy().subscribe(data=>this.filmsall=data)
  }
}
