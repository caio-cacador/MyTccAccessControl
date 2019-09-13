var img_original = document.getElementById('img_original');
var snapshotCanvas = document.getElementById('snapshot');
var captureButton = document.getElementById('capture');


captureButton.addEventListener('click', function() {
  var context = snapshot.getContext('2d');
  // Draw the video frame to the canvas.
  context.drawImage(img_original, 0, 0, snapshotCanvas.width,
      snapshotCanvas.height);

  var imgBse64 = snapshotCanvas.toDataURL("image/jpeg");

  var image = document.createElement("img")
  image.setAttribute("src", imgBse64)


  var wrapper = document.querySelector('.fotos')
  wrapper.appendChild(image)

});
