// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake



function Aircrafts(type){
   if(type === "F-16"){
      this.type = "F-16";
      this.ammo = 0;
      this.maxAmmo = 8;
      this.baseDamage = 30;
      this.allDamage = this.ammo * this.baseDamage;
   };
   if(type === "F-35"){
      this.type = "F-35";
      this.ammo = 0;
      this.maxAmmo = 12;
      this.baseDamage = 50;
      this.allDamage = this.ammo * this.baseDamage;
   };

   Aircrafts.prototype.fight = function(){
      var damage = this.ammo * this.baseDamage;
      this.ammo = 0;
      this.allDamage = this.ammo * this.baseDamage;
      return damage


   };



   Aircrafts.prototype.refill = function(number){
      if((this.ammo + number) <= this.maxAmmo){
         this.ammo += number;
         this.allDamage = this.ammo * this.baseDamage;
      }else{
         var remindAmmo = this.ammo + number - this.maxAmmo
         this.ammo = this.maxAmmo;
         this.allDamage = this.ammo * this.baseDamage;
         return remindAmmo
      }
   };


}


// Aircrafts.prototype.add_aircraft = function(){
//
// }




function Carrier(){
   this.healthPoints = 3000;
   this.ammoLoaded = 10;
   this.storeAircraft = [];
};

Carrier.prototype.add_aircraft = function(plane){
   this.storeAircraft.push(plane)
}

Carrier.prototype.fill = function(){
   battleship.storeAircraft.forEach(function(element) {
      if(battleship.ammoLoaded > element.maxAmmo-element.ammo){
   battleship.ammoLoaded -= (element.maxAmmo-element.ammo);
   element.ammo = element.maxAmmo;
   return battleship.ammoLoaded;
}else{
   return Error("not enough ammo")
   // return "we dont have enough ammo"
}

});
};
Carrier.prototype.fight = function(){
   var damage = 0;
   battleship.storeAircraft.forEach(function(element) {
   damage += (element.baseDamage * element.ammo);
   element.ammo = 0;
});
return Error("not enough ammo")
};

var plane1 = new Aircrafts('F-16');
var plane2 = new Aircrafts('F-35');

var battleship = new Carrier();

battleship.add_aircraft(plane1);
battleship.add_aircraft(plane2);

console.log(plane1);
// plane1.refill(4);
// plane1.refill(12);
console.log(plane1);
// plane2.refill(4);
// plane2.refill(12);
console.log(plane2);
console.log(battleship);

battleship.fill(4);
console.log(battleship.ammoLoaded);

// console.log(battleship.fight());
battleship.fight()
