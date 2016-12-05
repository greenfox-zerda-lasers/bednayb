'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)




function minimal(list1){
   min = list1[0];
   for( i = 0; i < list1.length-1; i++){
      min = Math.min(list1[i],list1[i+1])
   }
   console.log(min)
}

minimal(numbers)
