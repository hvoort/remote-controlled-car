<?php
// outputs the username that owns the running php/httpd process
// (on a system with the "whoami" executable in the path)

$move = $_GET['move'];
$direction = $_GET['direction'];
$speed = $_GET['speed'];

$play = $_GET['play'];
$song = $_GET['song'];

$faf = " > /dev/null & ";

// CONFIG
if (isset($move) && in_array($direction, array("LEFT", "RIGHT"))) {
  $play="t";
  $song="knipper.mp3";
}

// PLAY
if (isset($play)) {
  echo exec('(cd /home/pi/crazydriver/music/ && sudo ./play.sh ./'.$song.')'.$faf);
}

// MOVE
if (isset($move)) {
  if ($song="knipper.mp3") {
    usleep(1000);
  }
  echo exec('sudo python /home/pi/crazydriver/move.py '.$direction.' '.$speed.' 0.4'.$faf);
}



?>
