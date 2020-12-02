const imageContainer = document.querySelector("section.container#inf-img");
const modal = document.querySelector("div#modal");

/*
	* Paginated 
	* */
var page = 1;

function moreCancer(){
	var req = 'http://127.0.0.1:5000/all/' + page.toString();
		fetch(req, {mode: "cors"})
			.then(response => response.json())
			.then(data => {
				console.log(data)
				for (const image of data.data) {
					displayImage(image);
				}
			});
		page++;
	}

function displayModal(image) {
	modal.style.display = "block";
	img = modal.querySelector("img");
	img.src = image.image;
	img.alt = image.title;
	caption = modal.querySelector("#caption");
	caption.innerText = image.title;
	source = modal.querySelector("#source");
	source.innerText = image.host;
	source.href = image.original;
	close = modal.querySelector("#close-modal")
	close.onclick = function() {
		modal.style.display = "none";
	}
	console.log(modal)
	console.log(modal)
	console.log(modal)
}


/*
	* Create an image element in the HTML with the information provided
	* */	
function displayImage(image) {
	const div = document.createElement("div");
	const span = document.createElement("span");
	const img = document.createElement("img");

	img.src = image.image;
	img.alt = image.title;
	img.className = "container__img";

	span.className = "title";
	span.innerText = image.title;

	div.appendChild(img);
	div.appendChild(span);

	div.addEventListener("click", function() {
		displayModal(image);
	})

	imageContainer.appendChild(div);
	console.log('success')
}


fetch('http://127.0.0.1:5000/all/0', {mode: "cors"})
	.then(response => response.json())
	.then(data => {
		console.log(data)
		for (const image of data.data) {
			displayImage(image);
		}
	});
