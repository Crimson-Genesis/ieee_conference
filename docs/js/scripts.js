// carousel animations
const carouselFrames = Array.from(document.querySelectorAll('.carousel-frame'));

function makeCarousel(frame) {
  const carouselSlide = frame.querySelector('.carousel-slide');
  const carouselImages = getImagesPlusClones();
  const prevBtn = frame.querySelector('.carousel-prev');
  const nextBtn = frame.querySelector('.carousel-next');
  const navDots = Array.from(frame.querySelectorAll('.carousel-dots li'));

  let imageCounter = 1;

  function getImagesPlusClones() {
    let images = frame.querySelectorAll('.carousel-slide img');

    const firstClone = images[0].cloneNode();
    const lastClone = images[images.length - 1].cloneNode();

    firstClone.className = 'first-clone';
    lastClone.className = 'last-clone';

    // we need clones to make an infinite loop effect
    carouselSlide.append(firstClone);
    carouselSlide.prepend(lastClone);

    // must reassign images to include the newly cloned images
    images = frame.querySelectorAll('.carousel-slide img');

    return images;
  }

  function initializeNavDots() {
    if (navDots.length) navDots[0].classList.add('active-dot');
  }

  function initializeCarousel() {
    carouselSlide.style.transform = 'translateX(-100%)';
  }

  function slideForward() {
    // first limit counter to prevent fast-change bugs
    if (imageCounter >= carouselImages.length - 1) return;
    carouselSlide.style.transition = 'transform 400ms';
    imageCounter++;
    carouselSlide.style.transform = `translateX(-${100 * imageCounter}%)`;
  }

  function slideBack() {
    // first limit counter to prevent fast-change bugs
    if (imageCounter <= 0) return;
    carouselSlide.style.transition = 'transform 400ms';
    imageCounter--;
    carouselSlide.style.transform = `translateX(-${100 * imageCounter}%)`;
  }

  function makeLoop() {
    // instantly move from clones to originals to produce 'infinite-loop' effect
    if (carouselImages[imageCounter].classList.contains('last-clone')) {
      carouselSlide.style.transition = 'none';
      imageCounter = carouselImages.length - 2;
      carouselSlide.style.transform = `translateX(-${100 * imageCounter}%)`;
    }

    if (carouselImages[imageCounter].classList.contains('first-clone')) {
      carouselSlide.style.transition = 'none';
      imageCounter = carouselImages.length - imageCounter;
      carouselSlide.style.transform = `translateX(-${100 * imageCounter}%)`;
    }
  }

  function goToImage(e) {
    carouselSlide.style.transition = 'transform 400ms';
    imageCounter = 1 + navDots.indexOf(e.target);
    carouselSlide.style.transform = `translateX(-${100 * imageCounter}%)`;
  }

  function highlightCurrentDot() {
    navDots.forEach((dot) => {
      if (navDots.indexOf(dot) === imageCounter - 1) {
        dot.classList.add('active-dot');
      } else {
        dot.classList.remove('active-dot');
      }
    });
  }

  function addBtnListeners() {
    nextBtn.addEventListener('click', slideForward);
    prevBtn.addEventListener('click', slideBack);
  }

  function addNavDotListeners() {
    navDots.forEach((dot) => {
      dot.addEventListener('click', goToImage);
    });
  }

  function addTransitionListener() {
    carouselSlide.addEventListener('transitionend', () => {
      makeLoop();
      highlightCurrentDot();
    });
  }

  function autoAdvance() {
    let play = setInterval(slideForward, 5000);

    frame.addEventListener('mouseover', () => {
      clearInterval(play); // pause when mouse enters carousel
    });

    frame.addEventListener('mouseout', () => {
      play = setInterval(slideForward, 5000); // resume when mouse leaves carousel
    });

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        clearInterval(play); // pause when user leaves page
      } else {
        play = setInterval(slideForward, 5000); // resume when user returns to page
      }
    });
  }

  function buildCarousel() {
    initializeCarousel();
    initializeNavDots();
    addNavDotListeners();
    addBtnListeners();
    addTransitionListener();
    autoAdvance();
  }

  buildCarousel();
}

carouselFrames.forEach(frame => makeCarousel(frame));


// JavaScript code to generate bubbles
 document.addEventListener("DOMContentLoaded", function() {
  const bubblesContainer = document.querySelector('.bubbles');
  const bubbleCount = 128;
  
  for (let i = 0; i < bubbleCount; i++) {
    const bubble = document.createElement('div');
    bubble.classList.add('bubble');
    
    // Set random CSS variables for each bubble
    bubble.style.setProperty('--size', `${2 + Math.random() * 4}rem`);
    bubble.style.setProperty('--distance', `${6 + Math.random() * 4}rem`);
    bubble.style.setProperty('--position', `${-5 + Math.random() * 110}%`);
    bubble.style.setProperty('--time', `${2 + Math.random() * 2}s`);
    bubble.style.setProperty('--delay', `${-(2 + Math.random() * 2)}s`);
    
    bubblesContainer.appendChild(bubble);
  }
});

const scrollers = document.querySelectorAll(".scroller");

if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches ) {
  addAnimation();
  console.log("DATA attr set");
}
else {
  console.log("something went wrong");
}

function addAnimation() {
  scrollers.forEach( (scroller) => {
    scroller.setAttribute("data-animated", true);

    const scrollerInner = scroller.querySelector(".scroller-inner");
    const scrollerContent = Array.from(scrollerInner.children);

    scrollerContent.forEach(item =>{
      const duplicatedItem = item.cloneNode(true);
      duplicatedItem.setAttribute("aria-hidden",true);
      scrollerInner.appendChild(duplicatedItem);
    });
  });
}