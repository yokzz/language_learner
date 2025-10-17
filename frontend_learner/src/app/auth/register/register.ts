import { Component } from '@angular/core';
import {FormControl, ReactiveFormsModule} from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-register',
  imports: [ReactiveFormsModule],
  templateUrl: './register.html',
  styleUrl: './register.css'
})
export class Register {
  constructor(private http:HttpClient) {
    
  }

  name = new FormControl('');
  updateName() {
    this.name.setValue('Nancy');
  }
}
