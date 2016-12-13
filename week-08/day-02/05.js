// Add a click event listener to a <button> and console.log its innerHTML

var button = document.querySelector("button");

button.addEventListener("click", function(){
    document.getElementById("demo").innerHTML = "Hello World";
});
