const images = [
    'static/img/hero1.jpg',
    'static/img/hero2.jpg',
    'static/img/hero3.jpg',
    'static/img/hero4.jpg',
    'static/img/hero5.jpg'
];
let currentImageIndex = 0;
const slideshow = document.getElementById('hero-slideshow');
const row1 = document.querySelector('div#firstrow');
const row2 = document.querySelector('div#secondrow');
let flag = false; 

function changeBackground() {
    slideshow.style.backgroundImage = `url(${images[currentImageIndex]})`;
    currentImageIndex = (currentImageIndex + 1) % images.length;
}

// setInterval(changeBackground, 10000); // Change image every 5 seconds
// changeBackground(); // Initial call to set the first image


function chnageGridItems() {
    if(flag){
        row1.classList.add('nodisplay');
        row1.classList.remove('appear');
        row2.classList.remove('nodisplay');
        row2.classList.add('appear');
        flag = false;
    }else{
        row2.classList.add('nodisplay');
        row2.classList.remove('appear');
        row1.classList.remove('nodisplay');
        row1.classList.add('appear')
        flag = true;
    }
}

function disAnimation(){
    if(flag){
        row1.classList.add('disapperAnimation');
        row2.classList.remove('disapperAnimation');
        
    }else{
        row2.classList.add('disapperAnimation');
        row1.classList.remove('disapperAnimation');
    }
}


setInterval(disAnimation, 9500); 
setInterval(chnageGridItems, 10000); // Change image every 5 seconds

chnageGridItems(); // Initial call to set the first image