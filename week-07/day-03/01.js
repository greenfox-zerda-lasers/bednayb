'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"


function dictonary(number){
   switch (number) {
      case 0:
         return "zero";
         break;
      case 1:
         return "one";
         break;
      case 2:
         return "two";
         break;
      case 3:
         return "three";
         break;
      case 4:
         return "four";
         break;
      case 5:
         return "five";
         break;

      default:
         return "many";
   }
}

dictonary(4);
dictonary(3);
dictonary(11);
