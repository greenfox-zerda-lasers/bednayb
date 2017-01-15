var myNinjaApp = angular.module('myNinjaApp', []);

myNinjaApp.controller('NinjaController', function($scope){
   $scope.message = "Names";

   $scope.bloodStone = [
      {name:'tomi', belt:'yellow', score:23, examPass:true},
      {name:'bence', belt:'green',score:43, examPass:false},
      {name:'gergo', belt:'black',score:53, examPass:true},
      {name:'bela',score:234, belt:'pink', examPass:false},
      {name:'jozsef',score:213, belt:'brown', examPass:true},
      {name:'brigi',score:232, belt:'blue', examPass:true}
      ];

      $scope.addStudent = function(){
         $scope.bloodStone.push({
            name:$scope.members.name,
            belt:$scope.members.belt,
            score:parseInt($scope.members.score),
            examPass:true
         })
         $scope.members.name ="",
         $scope.members.belt ="",
         $scope.members.score =""
      }


});
