'use strict';

let playlist = ["Purple_Drift.mp3","Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3","Ars_Sonor_-_02_-_Never_Give_Up.mp3"];

let audio = document.querySelector('#audio');
let controls = document.querySelector('.control-div');
let currentSong = 0;


// Play Event
document.querySelector('.play-btn').addEventListener('click', ()=>{
        playPause();
    });
// Pause Event
audio.addEventListener('click', ()=>{
    playPause();
});

// PLAY/PAUSE
let playPause = ()=> {
    if (audio.paused) {
        audio.play();
        document.querySelector('.play-btn')
            .innerHTML = "<img src='images/play.svg' />";
    } else {
        audio.pause();
        document.querySelector('.play-btn').innerHTML = "<img src='images/pause.svg' />";
    }
}

// jump by time  BONUS
document.querySelector('.forward-btn')
    .addEventListener('click', ()=>{
        audio.currentTime = audio.currentTime + 10;
    });
document.querySelector('.backward-btn')
    .addEventListener('click', ()=>{
        audio.currentTime = audio.currentTime - 10;
    });



// jump by songs (+-1)
document.querySelector('.prev-song')
    .addEventListener('click', ()=>{
      if (currentSong != 0){
      currentSong -= 1;
   }
   console.log(currentSong);
        audio.src = playlist[currentSong];
     });

document.querySelector('.next-song')
    .addEventListener('click', ()=>{
      if(currentSong != playlist.length){
      currentSong += 1
   }
        audio.src = playlist[currentSong];
     });

////////ICONS////////

document.querySelector('.plus-icon').addEventListener('click', ()=>{
      console.log('plus');
});

document.querySelector('.star-icon').addEventListener('click', ()=>{
      console.log('star');
});
document.querySelector('.playlist-plus-icon').addEventListener('click', ()=>{
      console.log('playlist-star');
});
