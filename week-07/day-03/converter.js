'use strict';

// Create an object that has several converter methods:
// float2string(num) it should convert a float number to a string, for example 12.24 -> '12.24'
// string2float(str) it should convert a string to a float number, for example '12.24' -> 12.24
// int2roman(number) it should convert an int number to a roman number as a string, for example 12 -> 'XII'
// roman2int(number) it should convert a roman number as a string to an int, for example 'XII' -> 12 please try to avoid using the built in conversion methods


var converter = {


   float2string: function(element){
      return element.toString();
   },
   string2float: function(element){
      return parseFloat(element)
   },
   int2roman: function(element){
      var romainNumber = [];
      // CHECK VALID ELEMENT OR NOT
      if(element >= 1 && element <4000 && element % 1 == 0){
         // DIVIDE 1000
         var floorDivide1000 = Math.floor(element/1000);
         for(var i=0; i < floorDivide1000; i++){
            romainNumber.push("M")
         };
         element -= floorDivide1000 * 1000
         // DIVIDE 900
         var floorDivide900 = Math.floor(element/900);
         for(var i=0; i < floorDivide900; i++){
            romainNumber.push("CM")
         };
         element -= floorDivide900 * 900
         // DIVIDE 500
         var floorDivide500 = Math.floor(element/500);
         for(var i=0; i < floorDivide500; i++){
            romainNumber.push("D")
         };
         element -= floorDivide500 * 500
         // DIVIDE 400
         var floorDivide400 = Math.floor(element/400);
         for(var i=0; i < floorDivide400; i++){
            romainNumber.push("CD")
         };
         element -= floorDivide400 * 400
         // DIVIDE 100
         var floorDivide100 = Math.floor(element/100);
         for(var i=0; i < floorDivide100; i++){
            romainNumber.push("C")
         };
         element -= floorDivide100 * 100
         // DIVIDE 90
         var floorDivide90 = Math.floor(element/90);
         for(var i=0; i < floorDivide90; i++){
            romainNumber.push("XC")
         };
         element -= floorDivide90 * 90
         // DIVIDE 50
         var floorDivide50 = Math.floor(element/50);
         for(var i=0; i < floorDivide50; i++){
            romainNumber.push("L")
         };
         element -= floorDivide50 * 50
         // DIVIDE 40
         var floorDivide40 = Math.floor(element/40);
         for(var i=0; i < floorDivide40; i++){
            romainNumber.push("XL")
         };
         element -= floorDivide40 * 40
         // DIVIDE 10
         var floorDivide10 = Math.floor(element/10);
         for(var i=0; i < floorDivide10; i++){
            romainNumber.push("X")
         };
         element -= floorDivide10 * 10
         // DIVIDE 9
         var floorDivide9 = Math.floor(element/9);
         for(var i=0; i < floorDivide9; i++){
            romainNumber.push("IX")
         };
         element -= floorDivide9 * 9
         // DIVIDE 5
         var floorDivide5 = Math.floor(element/5);
         for(var i=0; i < floorDivide5; i++){
            romainNumber.push("V")
         };
         element -= floorDivide5 * 5
         // DIVIDE 4
         var floorDivide4 = Math.floor(element/4);
         for(var i=0; i < floorDivide4; i++){
            romainNumber.push("IV")
         };
         element -= floorDivide4 * 4
         // DIVIDE 1
         var floorDivide1 = Math.floor(element/1);
         for(var i=0; i < floorDivide1; i++){
            romainNumber.push("I")
         };
         element -= floorDivide1 * 1

         return romainNumber.join('')
      }else{
         return "I cant convert this element"
      }


   },
   roman2int: function(romainNumber){
      var normalNumber = 0;
      var romainNumberToList = romainNumber.split("");
      return romainNumberToList
   }

}



console.log(converter.float2string(2));
console.log(converter.string2float("4"));
console.log(converter.int2roman(3934));
console.log(converter.roman2int("MMMC"));
