'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades


var student = {

   grades: [],
   addgrade: function(grade){
      if(grade <=5 && grade >= 1 && grade % 1 == 0){
      this.grades.push(grade)
   }
   },
   getAverage: function(){
      var sum = 0;
      for(var i = 0; i < this.grades.length; i++){
         sum += this.grades[i]
      }
      return sum/this.grades.length

   }
}

student.addgrade(2);
student.addgrade(3);
student.addgrade(1);
student.addgrade(5);
student.addgrade(4);
console.log(student.grades);

console.log(student.getAverage());
