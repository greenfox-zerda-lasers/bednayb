'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

function sum(list){
   var summa = 0;
   for(var i = 0; i < list.length; i++){
      
      summa += list[i]
   }
   console.log(summa)
}

sum(numbers)
