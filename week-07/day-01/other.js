



var alma = function(){
   console.log("alma");
}


korte()

function korte(){
   console.log("korte");
}



function citrom(dinnye){
   dinnye()
}

citrom(alma)
citrom(korte)


// what is the difference?


var cica = [4,5,6,7,8,6];

kutya = cica.length

console.log(kutya);
console.log(cica);

cica.push(4);
console.log(cica);

console.log(cica.indexOf(6));
console.log("found,this is the",cica.indexOf(6),"th elem");

// nice solution
console.log("found:",cica.indexOf(6) != -1);
console.log("found:",cica.indexOf(11) != -1);

// FILTER
var arrr = [
    {"name":"apple", "count": 2},
    {"name":"orange", "count": 5},
    {"name":"pear", "count": 3},
    {"name":"orange", "count": 16},
];

var newArr = arrr.filter(function(item){
    if( item.name === "orange"){
      console.log(item.name,item.count);
   }
});

// FOR EACH

var arr = [1,2,3,4,5,6,7,8];

// Uses the usual "for" loop to iterate
for(var i = 0, l = arr.length; i< l; i++){
	console.log(arr[i]);
}

console.log("========================");

//Uses forEach to iterate
arr.forEach(function(item,index){
	console.log(item);
});
