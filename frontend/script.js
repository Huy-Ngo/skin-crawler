const imageContainer = document.querySelector("section.container#inf-img");

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
	img.className = "skinImage";

	span.className = "title";
	span.innerText = image.title;

	div.appendChild(img);
	div.appendChild(span);

	imageContainer.appendChild(div);
	console.log('success')
}

//Create the Modal
function displayModal(image){
	const div = document.createElement("div");
	const div_c = document.createElement("div");
	const div_s = document.createElement("div");
	const span = document.createElement("span");
	const img = document.createElement("img");

	div.id = "myModal";
	div.className = "modal";

	span.className = "close";
	span.innerText = "X";

	img.className = "modal-content";
	img.id = "img-full";

	div_c.id = "caption";
	div_s.id = "source";

	div.appendChild(span);
	div.appendChild(img);
	div.appendChild(div_c);
	div.appendChild(div_s);

	imageContainer.appendChild(div);
	console.log('modal success');
}


fetch('http://127.0.0.1:5000/all/0', {mode: "cors"})
	.then(response => response.json())
	.then(data => {
		console.log(data)
		for (const image of data.data) {
			displayImage(image);
			displayModal(image);
		}
	});