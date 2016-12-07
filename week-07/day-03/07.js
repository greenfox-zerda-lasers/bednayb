'use strict';

var numbers = [3,7,8,4];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

 function checkPrime(arr){

    var checkprimes = arr.map(function(e){
      var primes = true
      for(var i = 2; i <= Math.ceil(Math.pow(e,0.5)); i++){
         if(e % i == 0){
            primes = false;
            return primes;
         }
      }
      return primes
  })
  var ItHasPrime = checkprimes.every(function(e) {
    return e === true;
  });

  return ItHasPrime

 };

console.log(checkPrime(numbers));
