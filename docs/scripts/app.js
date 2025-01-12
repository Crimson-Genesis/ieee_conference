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
  }  )
}