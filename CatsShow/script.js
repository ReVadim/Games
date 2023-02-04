const catImg = document.getElementById('image')
const catBtn = document.getElementById('cat-button')

showCat()
	

async function showCat() {

	if(document.getElementById('cat-show') !== null) {
		document.getElementById('cat-show').remove();
	}

	const config = {
		method: 'GET',
        headers:{
            'Content-Type':'application/json'
        }
	}

	const result = await fetch('https://api.thecatapi.com/v1/images/search', config)

		const data = await result.json()

		const new_image = document.createElement('img')
		// new_image.width = data[0].width
		// new_image.height = data[0].height
		new_image.src = data[0].url
		new_image.alt = 'new'
		new_image.id = 'cat-show'
		catImg.appendChild(new_image)

}

catBtn.addEventListener('click', showCat)