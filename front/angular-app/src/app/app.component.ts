import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title =  this.method();

  public  method():string
  {
    let a:string = "cool";
    return a;
  }

}
