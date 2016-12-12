'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole','belaa'];
// create a function that returns the shortest string
// from an array

function shortestString(list){
   var shortest = list[0].length;

   for(var i = 0; i < list.length-1; i++){
      if( list[i].length > list[i+1].length){
         shortest = list[i+1]
      }
   }
   console.log(shortest)
}

shortestString(names)
