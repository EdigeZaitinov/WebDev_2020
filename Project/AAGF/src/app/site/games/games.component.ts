import { Component, OnInit } from '@angular/core';
import { GamesService } from 'src/app/games.service';

@Component({
  selector: 'app-games',
  templateUrl: './games.component.html',
  styleUrls: ['./games.component.css']
})
export class GamesComponent implements OnInit {
  public gamesall=[];

  constructor(private gameService: GamesService) {
   }

  ngOnInit(): void {
    this.gameService.getGames_2020().subscribe(data => this.gamesall = data);
  }

  btn_games2020(){
    this.gameService.getGames_2020().subscribe(data => this.gamesall = data);
  }

  btn_games2019(): void {
    this.gameService.getGames_2019().subscribe(data => this.gamesall = data);
  }

  btn_games2018(){
    this.gameService.getGames_2018().subscribe(data => this.gamesall = data);
  }

  btn_games2017(){
    this.gameService.getGames_2017().subscribe(data => this.gamesall = data);
  }
}
