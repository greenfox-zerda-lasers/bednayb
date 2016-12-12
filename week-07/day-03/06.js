'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function checkTheLetters(string,letter){
  return string.split('').indexOf(letter) != -1
};

console.log("found:"+checkTheLetters("apple tree","b"));
