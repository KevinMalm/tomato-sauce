import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LocalCharacterComponent } from './local-character.component';

describe('LocalCharacterComponent', () => {
  let component: LocalCharacterComponent;
  let fixture: ComponentFixture<LocalCharacterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LocalCharacterComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LocalCharacterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
