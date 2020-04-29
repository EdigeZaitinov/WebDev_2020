import { Component, OnInit } from '@angular/core';
import {UsersService} from 'src/app/users.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  public reg_email="";
  public reg_password="";
  public user=[];

  constructor(private userService:UsersService) { }

  ngOnInit(): void {
  }
}
