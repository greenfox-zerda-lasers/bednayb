'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods




function Stack(elements) {

   this.size = function size(){
      return elements.length
   };
   this.push = function push(newElement){
      elements[elements.length] = newElement
   };
   this.pop = function pop(){
      console.log(elements);
      var lastelement = elements[elements.length-1];
      elements.length -= 1
      return lastelement

   };
  }




var stack = new Stack([3,4,4,5,5,6,6,7,88]);

stack.size()
console.log(stack.size());
stack.push(6);
console.log(stack.size());
stack.pop();
console.log(stack.size());
stack.push(4);
console.log(stack.size());
