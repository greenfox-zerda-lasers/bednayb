'use strict';

var addButton = document.querySelector("#addNewElement");
var inputText = document.querySelector("#inputItem");
var deleteButton = document.querySelector("#deleteButton");

////////////READY/////////////// ADD NEW TASK  ////////////////////////////////////////
function addNewTask(task){
   var xhr = new XMLHttpRequest();
   xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
   xhr.setRequestHeader('Content-Type', 'application/json')
   xhr.send(JSON.stringify({text: task}))
   xhr.onreadystatechange = ready;

   function ready (rsp) {
      if( xhr.readyState === XMLHttpRequest.DONE ){
         console.log(JSON.parse(xhr.response))
      }
   }
}
   // CALL BUTTON EVENT
   addButton.addEventListener("click", addElement);
   function addElement(){
      addNewTask(inputItem.value);
   }
///////////////////////////////// END OF ADD NEW TASK  ////////////////////////////////////////

/////////NOT READY////////////////////// CHECK THE STATUS  ////////////////////////////////////////////


function getNewElement(){
   var xhr = new XMLHttpRequest();
   xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
   xhr.send(null);
   xhr.onreadystatechange = ready;

   function ready (rsp) {
      if( xhr.readyState === XMLHttpRequest.DONE ) {
         console.log(xhr.response);
         var todoData = JSON.parse(xhr.response);
         DisplayItem(todoData);
      }
   }
   // MAKE A SETINTERVAL FUNCTION TO THE UPDATE
}getNewElement();

      function DisplayItem(Items){
         console.log(Items);
         Items.forEach(function(e, i) {
         var itemToView = document.createElement('li');
         var todoLabel = document.createElement('label');
         var todoText = document.createElement('p');

         todoLabel.setAttribute('class', 'todo-item');
         todoLabel.setAttribute('for', 'list-item-' + i);
         todoText.textContent = e.text;
      })
   }

//////////////////////////////// END OF CHECK THE STATUS //////////////////////////////////////

///////////NOT READY/////////// DELETE /////////////////////////////////////////////////////
deleteButton.addEventListener("click", deleteToDo('8'));


function deleteToDo(index) {
   let xhr = new XMLHttpRequest();
   let url = 'https://mysterious-dusk-8248.herokuapp.com/todos/'+index;
   xhr.open('DELETE', url, true);
   xhr.setRequestHeader('Accept', 'application/json');
   xhr.send();
}
///////////////////////////////// END OF DELETE //////////////////////////////////////////////
