'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function even_and_odd(list){
   var odd_list = [];
   var even_list = [];

   for(var i = 0; i<list.length; i++){
      if(list[i] % 2 == 0){
         even_list.push(list[i])
      }else if(list[i] % 2 == 1){
         odd_list.push(list[i])
      }
   }
   console.log( odd_list)
   console.log( even_list)


}

even_and_odd(numbers)
