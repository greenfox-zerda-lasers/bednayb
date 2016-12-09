'use strict';

// PICTURES
var imageFiles = ['luffy.png','franky.png','sanji.png','zoro.png','brook.png','nami.png'];


var   images_number = 0


var mainPicture = document.querySelector('#image-wrapper');
var navigation = document.querySelector('.navigation');

var slides = document.querySelectorAll('.container .item').length;



var minpic =  document.querySelector(".slides");

var minpic1 = document.querySelector("#slide-1");
var minpic2 = document.querySelector("#slide-2");
var minpic3 = document.querySelector("#slide-3");
var minpic4 = document.querySelector("#slide-4");
var minpic5 = document.querySelector("#slide-5");
var minpic6 = document.querySelector("#slide-6");

var rightclick =  document.querySelector("#next");
var leftclick =  document.querySelector("#prev");



minpic1.addEventListener('click', function(){pictureNth(0)});
minpic2.addEventListener('click', function(){pictureNth(1)});
minpic3.addEventListener('click', function(){pictureNth(2)});
minpic4.addEventListener('click', function(){pictureNth(3)});
minpic5.addEventListener('click', function(){pictureNth(4)});
minpic6.addEventListener('click', function(){pictureNth(5)});


rightclick.addEventListener('click',rightClick);
leftclick.addEventListener('click',leftClick);

var imageFile = imageFiles[0];

function pictureNth(imageNth){
   images_number = imageNth;
   mainPicture.style.backgroundImage = 'url(' + imageFiles[images_number]+')';
}

function rightClick(){
   mainPicture.style.backgroundImage = 'url(' + imageFiles[images_number] +')';
   if(images_number < 5){
      images_number += 1;
   }
}

function leftClick(){
   mainPicture.style.backgroundImage = 'url(' + imageFiles[images_number] +')';
   if(images_number > 0){
      images_number -= 1;
   }
}
