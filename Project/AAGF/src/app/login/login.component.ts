import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UsersService } from 'src/app/users.service';
import { UseExistingWebDriver } from 'protractor/built/driverProviders';
import { EmailValidator } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public email = "";
  public password = "";
  public user=[];
  isChecked = false;

  constructor(private router: Router, private userService: UsersService) { }

  ngOnInit(): void {
  }


  check_password() {
    this.userService.getUser(this.email, this.password).subscribe(data => this.user = data)
    console.log(this.user.length)
    let email1;
    let password1;
    this.user.forEach(userFunction)
    function userFunction(element, index, array) {
      email1=element.fields.email
      password1=element.fields.password
    }
    console.log(email1)
    console.log(password1)
    if (this.email == email1 && this.password == password1 && this.isChecked == true) {
      this.router.navigate(['/AAGF']);
    }
    else if (this.email == email1 && this.password == password1 && this.isChecked == false) {
      alert("please click checkbox")
    }
    else {
      alert("this password is wrong");
    }
  }
  checked() {
    this.isChecked = !this.isChecked
    console.log(this.isChecked);
  }
}
