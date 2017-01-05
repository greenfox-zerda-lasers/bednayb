'use strict';

//////////////////////////VARIABLES//////////////////////////

////////// Tracks  //////////



let playlist = [
               {id:1, name:"Purple_Drift.mp3", time: "3:29", author:"bela"},
               {id:2, name:"Sign.mp3", time: "4:08", author:"Flow"},
               {id:3, name:"CLOSER.mp3", time: "3:33", author:"Joe Inoue"},
               {id:4, name:"Ars_Sonor_-_02_-_Never_Give_Up.mp3", time: "2:15", author:"bendeguz"},
               {id:5, name:"Mennyország Tourist.mp3", time: "3:35", author:"Tankcsapda"},
               {id:6, name:"Purple_Drift.mp3", time: "3:29", author:"bela"}
];
let favorites = [
               {id:3, name:"CLOSER.mp3", time: "3:33", author:"Joe Inoue"},
               {id:4, name:"Ars_Sonor_-_02_-_Never_Give_Up.mp3", time: "2:15", author:"bendeguz"},
               {id:5, name:"Mennyország Tourist.mp3", time: "3:35", author:"Tankcsapda"},
];

let Allplaylist =[playlist,favorites];

// let other = [
//                {id:1, name:"Purple_Drift.mp3", time: "3:29", author:"bela"},
//                {id:2, name:"Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3", time: "2:55", author:"bandi"},
//                {id:3, name:"Ars_Sonor_-_02_-_Never_Give_Up.mp3", time: "2:15", author:"bendeguz"}
// ];
let currentSong = 0;


////////// Controller  //////////
let audio = document.querySelector('#audio');
let controls = document.querySelector('.control-div');
let playAndPause = document.querySelector('.play-btn');
let forward = document.querySelector('.forward-btn');
let backward = document.querySelector('.backward-btn');
let prevSong = document.querySelector('.prev-song');
let nextSong = document.querySelector('.next-song');

////////// CurrentlySong  //////////
let plusIcon = document.querySelector('.plus-icon');
let starIcon = document.querySelector('.star-icon');

let currentlySongName = document.querySelector(".currentlySongName");
let currentlyArtistName = document.querySelector(".currentlyArtistName");
////////// Playlist  //////////
let addPlaylist = document.querySelector('.playlist-plus-icon');
   ///// Permanent lists //////
let tracks = document.querySelector('#tracks');
let everyplaylists = document.querySelector('.everyplaylists');
let playlistAllSong = document.querySelector('#playlist-All-tracks');
let playlistFavorites = document.querySelector('#playlist-Favorites');
////////// DeleteIcons  //////////
let deleteIcons = document.querySelector('.delete-icon');

// Play Event
playAndPause.addEventListener('click', ()=>{
        playPause();
    });
// Pause Event
audio.addEventListener('click', ()=>{
    playPause();
});

////////////////////////// EVENTS//////////////////////////

// JUMP TIME FORWARD (BONUS)
forward.addEventListener('click', ()=>{
  audio.currentTime = audio.currentTime + 10;
});

// JUMP TIME BACKWARD (BONUS)
backward.addEventListener('click', ()=>{
  audio.currentTime = audio.currentTime - 10;
});

// CHANGE THE SONG
prevSong.addEventListener('click', ()=>{
  if(currentSong !== 0){
   currentSong -= 1;
   }
   audio.src = playlist[currentSong].name;
});

nextSong.addEventListener('click', ()=>{
  if(currentSong != playlist.length - 1){
    currentSong += 1;
   //  console.log(currentSong);
    console.log(playlist[currentSong].name);
     currentlySongName.innerHTML =  playlist[currentSong].name;
     currentlyArtistName.innerHTML = playlist[currentSong].author;

    }
    audio.src = playlist[currentSong].name;
});



////////ICON EVENTS (not ready)////////
plusIcon.addEventListener('click', ()=>{
   console.log('plus');
});
starIcon.addEventListener('click', ()=>{
   console.log('star');
});

// Add playlist
addPlaylist.addEventListener('click', ()=>{
   let playLists = document.querySelector('.playlists');
   let name = prompt("What is the new Playlist's name?");
   console.log('playlist-star');
   let task = document.createElement('li');
   task.className = 'everyplaylists';
   task.setAttribute("id","folder-"+ name);
   // dragable
   task.setAttribute('draggable', 'true');
   task.setAttribute('ondragstart', 'drag(event)');

   // dragable

   playLists.appendChild(task);
   task.innerHTML = name;
   let deleteIcon = document.createElement('img');
   deleteIcon.setAttribute('class',"delete-icon");
   deleteIcon.setAttribute("id", "delete-" + name);
   deleteIcon.src = 'images/plus.svg';
   task.appendChild(deleteIcon);

   console.log(Allplaylist);
   var newlist = ["alma"];
   Allplaylist.push(newlist);
   console.log(Allplaylist[2][0]);



   deleteIcon.addEventListener('click', ()=>{

      let x = document.getElementById("folder-"+name).id;
      document.getElementById(x).remove();

   });
});

//////////FUNCTIONS ////////////////////

//LOAD THE FIRST SONG

let PlaytheSong = ()=>{
   audio.src = playlist[currentSong].name;
};PlaytheSong();

// PLAY/PAUSE FUNCTION
let playPause = ()=>{
   if (audio.paused) {
      audio.play();
      playAndPause.innerHTML = "<img src='images/play.svg' />";
   } else {
      audio.pause();
      playAndPause.innerHTML = "<img src='images/pause.svg' />";
   }
};

// ADD NEW PLAYLIST ELEMENT FUNCTION

// LIST PLAYLISTS ON LEFT PANEL

// LOAD the list to the right panel

playlistAllSong.addEventListener('click', ()=>{
   document.getElementById("songsOfFolder").remove();

   let newOl  = document.createElement('ol');
   newOl.setAttribute('id','songsOfFolder');
   tracks.appendChild(newOl);


   let playLists = document.querySelector('#songsOfFolder');
   for(let i = 0; i < playlist.length; i++){

      let task = document.createElement('li');
      task.setAttribute('class','currentlySongList');
      // task.className = 'song-'+ name;
      // task.setAttribute("id","song-"+ name);
      // newOl.appendChild(task);
      playLists.appendChild(task);
      task.innerHTML = playlist[i].name + "     " + playlist[i].time;

   }
});


playlistFavorites.addEventListener('click', ()=>{

   document.getElementById("songsOfFolder").remove();

   let newOl  = document.createElement('ol');
   newOl.setAttribute('id','songsOfFolder');
   tracks.appendChild(newOl);



   let playLists = document.querySelector('#songsOfFolder');
   for(let i = 0; i < favorites.length; i++){

      let task = document.createElement('li');
      task.setAttribute('class','currentlySongList');

      // make the element to dragable
      // dragable
      task.setAttribute('id',"alma-"+i)
      task.setAttribute('draggable', 'true');
      task.setAttribute('ondragstart', 'drag(event)');

      // dragable


      playLists.appendChild(task);
      task.innerHTML = favorites[i].name + "     " + favorites[i].time;
   }
});


function allowDrop(ev) {
   ev.preventDefault();
}

function drag(ev) {
   ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
   ev.preventDefault();
   var data = ev.dataTransfer.getData("text");
   ev.target.appendChild(document.getElementById(data));
}
