const imageContainer = document.querySelector("section.container#inf-img");

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
