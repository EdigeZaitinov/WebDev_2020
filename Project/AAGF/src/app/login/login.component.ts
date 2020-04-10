import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public email="";
  public password="";
  isChecked=false;

  constructor(private router:Router) { }

  ngOnInit(): void {
  }
  check_password(){
    console.log(this.email);
    if(this.email=="edige" && this.password==",jhtw" && this.isChecked==true){
      this.router.navigate(['/AAGF']);
    }
    else if(this.email=="edige" && this.password==",jhtw" && this.isChecked==false){
      alert("please click checkbox")
    }
    else{
      this.router.navigate(['']);
      alert("this password is wrong");
    }
  }
  checked(){
    this.isChecked=!this.isChecked
    console.log(this.isChecked);
  }

}
