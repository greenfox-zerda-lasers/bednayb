'use strict';

//////////////////////////VARIABLES//////////////////////////

////////// Tracks  //////////
let playlist = [
               {id:1, name:"Purple_Drift.mp3", time: "3:29", author:"bela"},
               {id:2, name:"Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3", time: "2:55", author:"bandi"},
               {id:3, name:"Ars_Sonor_-_02_-_Never_Give_Up.mp3", time: "2:15", author:"bendeguz"}
];
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
////////// Playlist  //////////
let addPlaylist = document.querySelector('.playlist-plus-icon');

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
   task.className = 'playlist-'+ name;

   playLists.appendChild(task);
   task.innerHTML = name;
   let deleteIcon = document.createElement('img');
   deleteIcon.className = "delete-icon" + ' '+ 'delete-'+ name;
   deleteIcon.src = 'images/plus.svg';
   task.appendChild(deleteIcon);

});


//////////FUNCTIONS ////////////////////

//LOAD THE FIRST SONG

let firstSong = ()=>{
   audio.src = playlist[currentSong].name;
};firstSong();

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
