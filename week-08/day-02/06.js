// Add an event listener to the window and display the mouse's x, y coordinates


var cursorX;
var cursorY;

window.onmousemove = function(e){
   cursorX = e.pageX;
   cursorY = e.pageY;
}

window.addEventListener("onmousemove",checkCursor);


function checkCursor(){
   console.log("Cursor at: " + cursorX + ", " + cursorY);
}
