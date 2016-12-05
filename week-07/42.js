'use strict';

// create a function that returns it's input factorial


function factorial(number){
   var fact = 1;
   for(var i = number; i >0 ; i--){
      fact *= i
   }
   console.log(fact)
}

factorial(5)
