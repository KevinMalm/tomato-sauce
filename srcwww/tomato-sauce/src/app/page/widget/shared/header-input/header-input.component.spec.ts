import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeaderInputComponent } from './header-input.component';

describe('HeaderInputComponent', () => {
  let component: HeaderInputComponent;
  let fixture: ComponentFixture<HeaderInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeaderInputComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeaderInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
