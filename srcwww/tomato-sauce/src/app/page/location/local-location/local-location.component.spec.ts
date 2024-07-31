import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LocalLocationComponent } from './local-location.component';

describe('LocalLocationComponent', () => {
  let component: LocalLocationComponent;
  let fixture: ComponentFixture<LocalLocationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [LocalLocationComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(LocalLocationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
