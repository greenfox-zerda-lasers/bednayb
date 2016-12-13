// Find the HTML skeleton of the game in the candy game folder.
//
// Gather 10.000 candies!
// Clicking the ‘Create candies’ button gives you 1 candy.
// You can buy a lollipop for 100 candies by clicking the ‘Buy lollipop’ button.
// 10 lollipops generate 1 candy per second.
// Use the 🍭 emoji to display the lollipops you have
// Display the candy producton rate in the Candies / Second row
// Create a procedural and OO versions of the same app

var createCandy = document.querySelector(".create-candies");
var buyLollipop = document.querySelector(".buy-lollypops");
var candyMachine = document.querySelector(".candy-machine");

var candy = 0;
var lollipop = 0;
var candyPerSec = 0;

createCandy.addEventListener("click", giveOneCandy);
buyLollipop.addEventListener("click", buyLollypops);
candyMachine.addEventListener("click", buyLollypops);

function giveOneCandy(){
   candy += 1;
    document.querySelector(".candies").innerHTML = candy;
};

function buyLollypops(){
   if(candy >= 3){
      candy -= 3;
      lollipop += 1;
       document.querySelector(".lollypops").innerHTML = lollipop + " 🍭🍭🍭";
       document.querySelector(".candies").innerHTML = candy;

   }
};



function generateCandy(){
   var plusCandy = Math.floor(lollipop /10);
   candy += plusCandy;
   document.querySelector(".candies").innerHTML = candy;
   document.querySelector(".speed").innerHTML = plusCandy;
   if(candy > 10000){
      alert("you win")
   }
   setTimeout(generateCandy,1000)
};
generateCandy();
