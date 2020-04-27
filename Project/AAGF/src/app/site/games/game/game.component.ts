import { Component, OnInit } from '@angular/core';
import { GamesService } from 'src/app/games.service';
import { ActivatedRoute, Router, ParamMap } from '@angular/router';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {
  public game=[]
  public game_name:string;
  constructor(private gameService: GamesService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe((params: ParamMap) => {
      let game_name = params.get('gameName').toString();
      this.game_name=game_name
    });
    this.gameService.getGame(this.game_name).subscribe(data => this.game = data);
  }

}
