'use strict';

////////// Tracks  //////////
let playlist = ["Purple_Drift.mp3","Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3","Ars_Sonor_-_02_-_Never_Give_Up.mp3"];
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

//////////////////////////CONTROLLER EVENTS//////////////////////////

// JUMP TIME (BONUS)
forward.addEventListener('click', ()=>{
  audio.currentTime = audio.currentTime + 10;
});

backward.addEventListener('click', ()=>{
  audio.currentTime = audio.currentTime - 10;
});

// CHANGE THE SONG
prevSong.addEventListener('click', ()=>{
  if(currentSong != 0){
   currentSong -= 1;
}
audio.src = playlist[currentSong];
     });

nextSong.addEventListener('click', ()=>{
  if(currentSong != playlist.length - 1){
    currentSong += 1
    }
    audio.src = playlist[currentSong];
     });

////////ICON EVENTS (not ready)////////
plusIcon.addEventListener('click', ()=>{
   console.log('plus');
});
starIcon.addEventListener('click', ()=>{
   console.log('star');
});
addPlaylist.addEventListener('click', ()=>{
   console.log('playlist-star');
});

// PLAY/PAUSE FUNCTION
let playPause = ()=>{
   if (audio.paused) {
      audio.play();
      playAndPause.innerHTML = "<img src='images/play.svg' />";
   } else {
      audio.pause();
      playAndPause.innerHTML = "<img src='images/pause.svg' />";
   }
}
