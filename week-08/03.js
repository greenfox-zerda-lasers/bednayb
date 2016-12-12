'use strict';

// Create a constructor for creating Rockets.

// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)

// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)


function Rockets(consumption){
   this.consumption = consumption;
   this.amount = 0;
   this.launchNumber = 0;

}

Rockets.prototype.fill = function(){
    this.amount += this.consumption;
    console.log("amount", this.amount);
    return this.amount;
};

Rockets.prototype.launch = function(){
   if(this.amount >= this.consumption){
      this.launchNumber += 1;
      this.amount -= this.consumption;
   }
   console.log(this.launchNumber);
};

var rocket1 = new Rockets(300);


rocket1.fill();
rocket1.launch();
