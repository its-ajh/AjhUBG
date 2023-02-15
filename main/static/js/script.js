var elem = document.documentElement;

/* View in fullscreen */
function fullscreen() {
  document.getElementsByTagName("iframe")[0].className = "fullScreen";
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.webkitRequestFullscreen) { /* Safari */
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { /* IE11 */
    elem.msRequestFullscreen();
  }
  document.addEventListener('fullscreenchange', ()=>{
    if (document.fullscreenElement) {
        console.log('Fullscreen');
    } else {
        closeFullscreen()
    }
});
}
/* Close fullscreen */
function closeFullscreen() {
  document.getElementsByTagName("iframe")[0].className = "";
  if (document.exitFullscreen) {
    document.exitFullscreen();
  } else if (document.webkitExitFullscreen) { /* Safari */
    document.webkitExitFullscreen();
  } else if (document.msExitFullscreen) { /* IE11 */
    document.msExitFullscreen();
  }
}
