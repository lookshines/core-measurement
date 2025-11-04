document.addEventListener("DOMContentLoaded", function() {
    const elements = document.querySelectorAll('.fade-up, .fade-right, .fade-left');


    function revealOnScroll() {
        const windowHeight = window.innerHeight;
        elements.forEach(re => {
            const positionFromTop = re.getBoundingClientRect().top;
            if (positionFromTop < windowHeight - 100) {
                re.classList.add('active');

            }
        });
    }

    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // trigger load
});

// == COUNTER SCRIPT == //

document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll("#funfact h1");
  let started = false; // ensures animation runs only once

  // Set all counters to show 0 initially
  counters.forEach(counter => counter.textContent = "0");

  function countUp(element, target) {
    let count = 0;
    const duration = 2000; // total animation time (ms)
    const step = Math.ceil(target / (duration / 20)); // increment per frame

    const interval = setInterval(() => {
      count += step;
      if (count >= target) {
        count = target;
        clearInterval(interval);
      }
      element.textContent = count;
    }, 20);
  }

  function startCounting() {
    const section = document.querySelector("#funfact");
    const sectionTop = section.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;

    if (sectionTop < windowHeight - 100 && !started) {
      started = true;
      counters.forEach(counter => {
        const target = parseInt(counter.getAttribute("data-target"));
        countUp(counter, target);
      });
    }
  }

  window.addEventListener("scroll", startCounting);
});

/* Back to Top Button */

  const backToTop = document.getElementById("backToTop");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
      backToTop.classList.add("show");
    } else {
      backToTop.classList.remove("show");
    }
  });

  backToTop.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  });

