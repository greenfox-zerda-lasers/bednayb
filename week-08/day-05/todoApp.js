'use strict';

var addButton = document.querySelector("#addNewElement");
var inputText = document.querySelector("#inputItem");
var deleteButton = document.querySelector(".deleteButton");



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

var alma = addNewTask(inputItem.value);
///////////////////////////////// END OF ADD NEW TASK  ////////////////////////////////////////

// // UPDATE//
setInterval(alma,3000);
// // UPDATE//




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
         
         Items.forEach(function(e, i) {

            var task = document.createElement('div');
            // var itemToView = document.createElement('li');
            var span = document.createElement('span');
            var todoLabel = document.createElement('label');
            var todoText = document.createElement('p');
            var trash = document.createElement('img');
            trash.id = e.id;
            trash.addEventListener("click", function(){
               deleteToDo(e.id)
            });
            var newCheckBox = document.createElement('input');
            trash.src = 'delete.png';
            newCheckBox.type = 'checkbox';


            listnewitem.appendChild(task);
            task.appendChild(span);
            span.appendChild(todoText);
            // span.appendChild(todoLabel);
            span.appendChild(trash);
            span.appendChild(newCheckBox);
            // itemToView.appendChild(todoText);

            todoText.innerHTML = e.text;
            // todoText.textContent = e.text;
            // task.innerHTML = e;

            // console.log(e);
            // console.log(i);
            // console.log(e.text);

            // setInterval(DisplayItem(Items), 2000);


            // todoLabel.setAttribute('class', 'todo-item');
            // todoLabel.setAttribute('for', 'list-item-' + i);
      })
   };

//////////////////////////////// END OF CHECK THE STATUS //////////////////////////////////////

///////////70% READY/////////// DELETE /////////////////////////////////////////////////////







function deleteToDo(index) {
   let xhr = new XMLHttpRequest();
   let url = 'https://mysterious-dusk-8248.herokuapp.com/todos/'+index;
   xhr.open('DELETE', url, true);
   xhr.setRequestHeader('Accept', 'application/json');
   xhr.send();
}
///////////////////////////////// END OF DELETE //////////////////////////////////////////////
