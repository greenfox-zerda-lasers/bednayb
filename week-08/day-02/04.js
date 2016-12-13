
// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)

var cursorX;
var cursorY;

document.onmousemove = function(e){
   cursorX = e.pageX;
   cursorY = e.pageY;
}

function checkCursor(){
   console.log("Cursor at: " + cursorX + ", " + cursorY);
   setTimeout(checkCursor, 1500);
}

checkCursor()
