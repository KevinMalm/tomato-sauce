import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { RestCharacterService } from '../../service/rest/interface/character.rest.interface';
import { result_is_ok } from '../../data/result.data';
import { Entity, ListEntitiesResponse } from '../../data/entity.data';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-character',
  standalone: true,
  imports: [
    CommonModule
  ],
  templateUrl: './character.component.html',
  styleUrl: './character.component.scss'
})
export class CharacterComponent {

  characters: Entity[] | null = null;

  constructor(private client: HttpClient) {

  }

  ngOnInit() {
    this.load_characters()
  }

  async load_characters() {
    let response = await RestCharacterService.load_characters(this.client);
    if (result_is_ok(response)) {
      this.characters = (response.body as ListEntitiesResponse).entities;
    } else {
      // TODO: Handle error
      console.log(response)
    }
  }
}
