'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

var tomb = [4,5,6,7,11];

function write_the_items(a){
   console.log(a);
};

function each(arr,func){
   arr.map(function(e){
      func(e);
   })
}


each(tomb,write_the_items)
