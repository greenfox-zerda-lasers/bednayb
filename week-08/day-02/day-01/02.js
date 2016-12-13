'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference



function Rectangle(side_a,side_b){
   this.side_a = side_a;
   this.side_b = side_b;
}

Rectangle.prototype.getArea = function(){
   return this.side_a * this.side_b
};
Rectangle.prototype.getCircumference = function(){
   return (this.side_a + this.side_b)*2
};

var smallRectange = new Rectangle(5,6);
var bigRectangle = new Rectangle(23,56);

console.log(smallRectange.getArea());
console.log(smallRectange.getCircumference());

console.log(bigRectangle.getArea());
console.log(bigRectangle.getCircumference());
