const collapsibles = document.querySelectorAll(".collapsible");
collapsibles.forEach((item) =>
  item.addEventListener("click", function () {
    this.classList.toggle("collapsible--expanded");
  })
);

// Slideshow

var slideshow__slides = document.querySelectorAll(".slideshow__slide");
var slideshow__btns = document.querySelectorAll(".slideshow__btn");
let currentslideshow__slide = 1;

// Javascript for image slideshow__slider manual slideshow__navigation
var manualNav = function (manual) {
  slideshow__slides.forEach((slideshow__slide) => {
    slideshow__slide.classList.remove("active");

    slideshow__btns.forEach((slideshow__btn) => {
      slideshow__btn.classList.remove("active");
    });
  });

  slideshow__slides[manual].classList.add("active");
  slideshow__btns[manual].classList.add("active");
};

slideshow__btns.forEach((slideshow__btn, i) => {
  slideshow__btn.addEventListener("click", () => {
    manualNav(i);
    currentslideshow__slide = i;
  });
});

// Javascript for image slideshow__slider autoplay slideshow__navigation
var repeat = function (activeClass) {
  let active = document.getElementsByClassName("active");
  let i = 1;

  var repeater = () => {
    setTimeout(function () {
      [...active].forEach((activeslideshow__slide) => {
        activeslideshow__slide.classList.remove("active");
      });

      slideshow__slides[i].classList.add("active");
      slideshow__btns[i].classList.add("active");
      i++;

      if (slideshow__slides.length == i) {
        i = 0;
      }
      if (i >= slideshow__slides.length) {
        return;
      }
      repeater();
    }, 5000);
  };
  repeater();
};
repeat();



/// Portfolio Carousel
document.addEventListener("DOMContentLoaded", () => {
  const carousel = document.querySelector(".review-carousel");
  let scrollAmount = 0;
  let direction = 1; // 1 for left-to-right, -1 for right-to-left
  let intervalId;

  function autoScroll() {
    scrollAmount += direction * 2; // Adjust this value to control speed
    if (
      scrollAmount >= carousel.scrollWidth - carousel.clientWidth ||
      scrollAmount <= 0
    ) {
      // Reverse direction when the end or start is reached
      direction *= -1;
    }
    carousel.scrollLeft = scrollAmount;
  }

  function startAutoScroll() {
    intervalId = setInterval(autoScroll, 60); // Adjust the speed by modifying the interval time
  }

  function stopAutoScroll() {
    clearInterval(intervalId);
  }

  // Intersection Observer to detect when the carousel is in view
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          startAutoScroll();
        } else {
          stopAutoScroll();
        }
      });
    },
    { threshold: 0.1 }
  ); // Adjust the threshold if needed

  // Observe the carousel element
  observer.observe(carousel);
});