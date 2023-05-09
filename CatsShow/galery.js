
const base = document.querySelector('.base')
const backBtn = document.getElementById('backBtn')
const forwardBtn = document.getElementById('backBtn')
const closeBtn = document.getElementById('closeBtn')
const pictures = document.querySelector('.pictures')
const LIKED_IMAGES_LS = 'liked'
const storageList = []


function showImages() {
   const images = localStorage.getItem(LIKED_IMAGES_LS)
   if (images !== null) {
      const imagesList = JSON.parse(images)
      imagesList.forEach(img => {
         createImg(img);
      })
   }
}

function createImg(img) {
   const itemCell = document.createElement('div')
   itemCell.classList.add('likedPicture')
   const new_image = document.createElement('img')
         new_image.src = img.url
         new_image.alt = img.url
         new_image.classList.add(`img-${img.id}`)
   const delBtn = document.createElement('button')
         delBtn.classList.add('dislike')
         delBtn.id = `img-${img.id}`
         delBtn.innerHTML = '❌'
   itemCell.appendChild(new_image)
   itemCell.appendChild(delBtn)
   pictures.appendChild(itemCell)
}

function checkDelButtons() {
   const delButtons = pictures.querySelectorAll('.dislike');
      delButtons.forEach(btn => {
         btn.addEventListener('click', () => {
            removeImage(btn.id);
         })
   })
}

function removeImage(imgClassName) {
   const img = document.getElementsByClassName(imgClassName)
   const img_cls = img[0].classList.value
   document.querySelector('.' + img_cls).remove()
   refreshLocalStorage();
}

function refreshLocalStorage() {
   const allImages = document.querySelectorAll('img')
         allImages.forEach(img => {
            console.log(img.alt)
            updateLS(img.alt)
         })
}

function saveLikeInLS() {
   data = JSON.stringify(storageList)
   localStorage.setItem(LIKED_IMAGES_LS, '');
   localStorage.setItem(LIKED_IMAGES_LS, data);
}

function updateLS(url) {
   const likeListItem = {
         id: storageList.length + 1, // задаем id для элемента
         url: url
      }
      storageList.push(likeListItem); // добавляем новый объект в массив
      saveLikeInLS();
}

function main() {
   showImages();
   checkDelButtons();
}

main()

