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