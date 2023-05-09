const left = document.querySelector('.left')
const right = document.querySelector('.right')
const container = document.querySelector('.container')
const catBtn = document.querySelector('.cat')
const dogBtn = document.querySelector('.dog')
const catsWorld = document.querySelector('.cats-world')
const dogsWorld = document.querySelector('.dogs-world')
const homePage= document.querySelectorAll('.homepage')

const dogBackBtn = document.getElementById('dogBackBtn')
const catBackBtn =document.getElementById('catBackBtn')

const showCatBtn = document.getElementById('showCatBtn')
const showDogBtn = document.getElementById('showDogBtn')

const showCatImage = document.querySelector('.showCatImage')
const showDogImage = document.querySelector('.showDogImage')

const catLikeBtn = document.getElementById('catlikeBtn')
const dogLikeBtn = document.getElementById('dogLikeBtn')

const DOG_API = 'https://dog.ceo/api/breeds/image/random'
const CAT_API = 'https://api.thecatapi.com/v1/images/search'

let catBackUrl = './img/cat.jpg'
let dogBackUrl = './img/jack-russel.jpg'

const lastDog = document.getElementById('lastDog')

let LIKED_IMAGES_LS = 'liked'
let likedList = []
const photoStockBtn = document.getElementById('photoStock')
const showPhotoStockBtn = document.querySelector('.photoStock')

checkLikedImages();

left.addEventListener('mouseenter', () => container.classList.add('hover-left'))
left.addEventListener('mouseleave', () => container.classList.remove('hover-left'))

right.addEventListener('mouseenter', () => container.classList.add('hover-right'))
right.addEventListener('mouseleave', () => container.classList.remove('hover-right'))


catBtn.addEventListener('click', () => {
	container.classList.add('up');
	dogsWorld.classList.add('up');
	return false
})

dogBtn.addEventListener('click', () => {
	container.classList.add('up');
	catsWorld.classList.add('up');
	return false
})

homePage.forEach(btn => {
	btn.addEventListener('click', () => {
		container.classList.remove('up');
		dogsWorld.classList.remove('up');
		catsWorld.classList.remove('up');
	})
})


async function catShow() {

	if(showCatImage !== null) {
		try {
		document.getElementById('cat-show').remove();}
		catch(error) {
		document.getElementById('lastCat').classList.add('hidden');}
	}

	const config = {
		method: 'GET',
        headers:{
            'Content-Type':'application/json'
        }
	}
	const result = await fetch(CAT_API, config)

		const data = await result.json()

		const new_image = document.createElement('img')
		new_image.src = data[0].url
		new_image.alt = 'new'
		new_image.id = 'cat-show'
		showCatImage.appendChild(new_image)
		catBackUrl = data[0].url
}

showCatBtn.addEventListener('click', () => {
	catShow();
	catBackBtn.classList.remove('hidden');
	catLikeBtn.classList.remove('hidden');
	catLikeBtn.classList.remove('liked');
	lastCat.classList.add('hidden');
	showLastCat(catBackUrl)
})

showDogBtn.addEventListener('click', () => {
	dogShow();
	dogBackBtn.classList.remove('hidden');
	dogLikeBtn.classList.remove('hidden');
	dogLikeBtn.classList.remove('liked');
	lastDog.classList.add('hidden');
	lastDog.src = dogBackUrl
})

function dogShow() {

	if(document.getElementById('dog-show') !== null) {
			document.getElementById('dog-show').remove();
		}
	fetch(DOG_API)
	  .then(res => {
	    return res.json();
	  })
	  .then(data => {
	    const breedsObject = data.message;
	    if(breedsObject === null) {
	    	const breedsObject = './img/jack-russel.jpg'}
	    const new_image = document.createElement('img')
			new_image.src = breedsObject
			new_image.alt = 'new'
			new_image.id = 'dog-show'
			showDogImage.appendChild(new_image)
			dogBackUrl = breedsObject
	  });
}

catBackBtn.addEventListener('click', () => {
	document.getElementById('lastCat').classList.remove('hidden')
	document.getElementById('cat-show').classList.add('hidden');
	document.getElementById('cat-show').src = '';
	catBackBtn.classList.add('hidden')
	lastCat = document.getElementById('lastCat')
	catBackUrl = lastCat.src
})

dogBackBtn.addEventListener('click', () => {
	lastDog.classList.remove('hidden');
	dogValues = document.getElementById('dog-show')
	dogValues.classList.add('hidden');
	dogValues.src = '';
	dogBackBtn.classList.add('hidden');
	dogBackUrl = lastDog.src
})

function showLastCat(url) {
	const lastCat = document.getElementById('lastCat')
	lastCat.src = url
}

catLikeBtn.addEventListener('click', () => {
	catLikeBtn.classList.add('liked')
	saveLike(catBackUrl)
	showPhotoStockBtn.classList.remove('hidden');
})

dogLikeBtn.addEventListener('click', () => {
	dogLikeBtn.classList.add('liked')
	saveLike(dogBackUrl)
	showPhotoStockBtn.classList.remove('hidden');
})

function getPhotoAlbum() {
	const likedImages = localStorage.getItem(LIKED_IMAGES_LS);
	if (likedImages !== null) {
		const parseImages = JSON.parse(likedImages)
		parseImages.forEach(image => {
			likedList.push(image);
		})
	}
}

function checkLikedImages() {
	const likedImages = localStorage.getItem(LIKED_IMAGES_LS);
	if(likedImages !== null) {
		getPhotoAlbum();
		showPhotoStockBtn.classList.remove('hidden');
	} else {
		showPhotoStockBtn.classList.add('hidden');
	}
}

photoStockBtn.addEventListener('click', getPhotoAlbum )


function saveLikeInLS() {
	data = JSON.stringify(likedList)
	localStorage.setItem(LIKED_IMAGES_LS, data);
}

function saveLike(url) {
	const likeListItem = {
			id: likedList.length + 1, // задаем id для элемента
			url: url
		}
		likedList.push(likeListItem); // добавляем новый объект в массив
		saveLikeInLS();
}