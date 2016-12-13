

var myVar;

function myFunction() {
    myVar = setTimeout(function(){ alert("Hello"); }, 3000);
}

function myStopFunction() {
    clearTimeout(myVar);
}
