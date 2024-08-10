import { Directive, Input, ElementRef, AfterViewInit } from '@angular/core';

@Directive({
  selector: '[appProgressSpinner]',
  standalone: true
})
export class ProgressSpinnerDirective implements AfterViewInit {

  @Input()
  color!: string;

  constructor(
    private elem: ElementRef
  ) { }

  ngAfterViewInit() {
    if (!!this.color) {
      const element = this.elem.nativeElement;
      const circles = element.querySelectorAll("circle");
      circles.forEach((circle: any) => {
        circle.style.stroke = this.color;
      });
    }
  }
}
