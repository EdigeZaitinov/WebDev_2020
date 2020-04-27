import { Component, OnInit } from '@angular/core';
import { FilmsService } from 'src/app/films.service';
import { ActivatedRoute, Router, ParamMap } from '@angular/router';

@Component({
  selector: 'app-film',
  templateUrl: './film.component.html',
  styleUrls: ['./film.component.css']
})
export class FilmComponent implements OnInit {

  public film=[]
  public film_name:string;
  constructor(private filmService: FilmsService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe((params: ParamMap) => {
      let film_name = params.get('filmName').toString();
      this.film_name=film_name
    });
    this.filmService.getFilm(this.film_name).subscribe(data => this.film = data);
  }

}
