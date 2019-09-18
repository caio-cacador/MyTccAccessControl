var img_original = document.getElementById('img_original');
var snapshotCanvas = document.getElementById('snapshot');
var captureButton = document.getElementById('capture');
var user_name = document.getElementById('id_name');

var list_field = document.querySelectorAll('textarea')
// for (var i = 1 ; i < list_field.length; i++) {
//       // console.log(list_field[i].setAttribute("style", 'display:none;'))
// }

var count = 0
captureButton.addEventListener('click', function() {
  var context = snapshot.getContext('2d');
  // Draw the video frame to the canvas.
  context.drawImage(img_original, 0, 0, snapshotCanvas.width,
      snapshotCanvas.height);

  var imgBse64 = snapshotCanvas.toDataURL("image/jpeg");

  console.log(list_field[count])
  list_field[count].textContent = imgBse64.toString()

  var image = document.createElement("img")
  var wrapper = document.querySelector('.fotos')
  image.setAttribute("src", imgBse64)
  image.setAttribute("id", (user_name.value + wrapper.childElementCount.toString()))

  if (wrapper.childElementCount < 6) {
    wrapper.appendChild(image)
  }
  count += 1
});
