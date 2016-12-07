'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}


function countLetters(string){
   var list = string.split("");
   var object = {};
     for(var i=0; i < string.length; i++){
        if(!object[list[i]]){
           object[list[i]] = 1;
        }else{
           object[list[i]] += 1
        }
     }



   console.log(object);
}

countLetters("almafa")















 // NICE SOLUTION

// function countLetters(string){
//    for(var i=0; i < string.length; i++){
//       console.log(string[i],":",string.split(string[i]).length-1);
//    }
// }
//
//
// countLetters("alma")
//
//
// console.log();
