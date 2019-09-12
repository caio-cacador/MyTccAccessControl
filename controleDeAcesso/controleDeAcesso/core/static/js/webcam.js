var player = document.getElementById('player');
var snapshotCanvas = document.getElementById('snapshot');
var captureButton = document.getElementById('capture');

var handleSuccess = function(stream) {
  // Attach the video stream to the video element and autoplay.
  player.srcObject = stream;
};

captureButton.addEventListener('click', function() {
  var context = snapshot.getContext('2d');
  // Draw the video frame to the canvas.
  context.drawImage(player, 0, 0, snapshotCanvas.width,
      snapshotCanvas.height);

  var imgBse64 = snapshotCanvas.toDataURL("image/jpeg");

  var image = document.createElement("img")
  image.setAttribute("src", imgBse64)


  var wrapper = document.querySelector('.fotos')
  wrapper.appendChild(image)

  //var arr = document.querySelectorAll('.fotos img')
});

navigator.mediaDevices.getUserMedia({video: true})
    .then(handleSuccess);