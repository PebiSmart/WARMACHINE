import { Component, OnInit } from '@angular/core';
import { Army } from 'src/army';
import { ARMIES } from '../mock-armies';

@Component({
  selector: 'app-armies',
  templateUrl: './armies.component.html',
  styleUrls: ['./armies.component.css']
})
export class ArmiesComponent {

  selectedArmy? : Army;

  onSelect(army: Army): void {
    this.selectedArmy = army
}

  armies = ARMIES;

  army : Army = {
    id: 1,
    name: 'test army',
    battleFactor: 100,
  }

}
