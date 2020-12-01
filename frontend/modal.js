// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var thumbnail = getElementsByClassName('skinImage');
var modalImg = $("#img-full");
var captionText = document.getElementById("caption");
$('.title').click(function(){
	modal.style.display = "block";
    var newSrc = thumbnail.src;
    modalImg.attr('src', newSrc);
    captionText.innerHTML = thumbnail.alt;
})

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}