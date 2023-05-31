import { Component, OnInit } from '@angular/core';
import { Army } from 'src/army';

@Component({
  selector: 'app-armies',
  templateUrl: './armies.component.html',
  styleUrls: ['./armies.component.css']
})
export class ArmiesComponent {

army : Army = {
  id: 1,
  name: 'test army',
  battleFactor: 100,
}

}
