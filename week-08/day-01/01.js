'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says


// var Animal = new Animals();

function Animals(says) {
   this.says = says;
}

Animals.prototype.say = function(){
   console.log(this.says);
}

var dog = new Animals("vhao");
var cat = new Animals("meow");

dog.say();
cat.say();
