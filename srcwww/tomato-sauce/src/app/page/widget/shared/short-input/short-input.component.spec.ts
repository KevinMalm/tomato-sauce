import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShortInputComponent } from './short-input.component';

describe('ShortInputComponent', () => {
  let component: ShortInputComponent;
  let fixture: ComponentFixture<ShortInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ShortInputComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShortInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
