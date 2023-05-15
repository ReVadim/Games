const body = document.body
const sliderContainer = document.querySelector('.slider-container')
const slides = document.querySelectorAll('.likedPicture')
const leftBtn = document.getElementById('backBtn')
const rightBtn = document.getElementById('forwardBtn')
const closeBtn = document.getElementById('closeBtn')
const allImages = pictures.querySelectorAll('img')

let urlList = []
let mainUrl = ''


pictures.addEventListener('click', look);

closeBtn.addEventListener('click', () => {
	sliderContainer.classList.add('hidden');
	pictures.classList.remove('hidden');
})

function look(event) {
   if(event.target.tagName == "IMG") {
      const backgroundSrc = event.target.src;
      createBackgroundImg(backgroundSrc);
      addToStockList();
      mainUrl = backgroundSrc;
		displayArrows(backgroundSrc);
      pictures.classList.add('hidden');
      sliderContainer.classList.remove('hidden');
   }
}

function createBackgroundImg(url) {
	const new_background = document.createElement('div');
		  new_background.classList.add('slide');
		  new_background.classList.add('active');
		  setBackgroundToBody(url)
		  new_background.style.backgroundImage = `url(${url})`;
		  sliderContainer.appendChild(new_background);
}

// function addToStockList() {
// 	allImages.forEach(function(img, index, array) {
// 		const data = {
// 			id: index,
// 			url: img.src
// 		}
// 	 urlList.push(data) });
// 	console.log(urlList)
// }

function displayArrows(url) {
	const imageNumber = urlList.indexOf(url)
	if (imageNumber === 0) {
		leftBtn.classList.add('hidden')
	} else {
		leftBtn.classList.remove('hidden')
	}
	if (imageNumber === (urlList.length - 1)) {
		rightBtn.classList.add('hidden')
	} else {
		rightBtn.classList.remove('hidden')
	}
}

function addToStockList() {
	allImages.forEach(img => urlList.push(img.src))
}

rightBtn.addEventListener('click', () => {

	const imageNumber = urlList.indexOf(mainUrl)

	if (imageNumber < urlList.length-1) {
		const nextUrl = urlList[+imageNumber + 1]
		createBackgroundImg(nextUrl);
		mainUrl = nextUrl;
		displayArrows(mainUrl);
	}
})

leftBtn.addEventListener('click', () => {
	const imageNumber = urlList.indexOf(mainUrl)
	if (imageNumber === 0) {
		createBackgroundImg(mainUrl);
	} else if (imageNumber > 0) {
		const nextUrl = urlList[+imageNumber - 1]
		createBackgroundImg(nextUrl);
		mainUrl = nextUrl;
		displayArrows(mainUrl);
	}
})

function setBackgroundToBody(url) {
	body.style.backgroundImage = `url(${url})`;
}

setBackgroundToBody()