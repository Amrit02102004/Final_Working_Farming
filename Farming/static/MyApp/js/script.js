// script.js

document.addEventListener("DOMContentLoaded", function () {
    var num = document.getElementById('numberDisplay');
    var body = document.body;
  
    var target = parseInt(document.querySelector('.num').getAttribute('data-target'));
    function updateBackground() {
      if (target <= 25) {
        body.classList.add("desert-bg");
      } else {
        body.classList.add("water-bg");
      }
    }
    updateBackground();
    if (target <= 25) {
      document.getElementById('image1').style.display = 'block';
    } else if (target >= 70) {
      document.getElementById('image2').style.display = 'block';
    } else {
      document.getElementById('image3').style.display = 'block';
    }
  
    const progressFill = document.querySelector('.progressFill');
    const block = document.getElementsByClassName('block');
    for (var i = 1; i < target; i++) {
      progressFill.innerHTML += "<div class='block'></div>";
      block[i].style.transform = "rotate(" + 3.6 * i + "deg)";
      block[i].style.animationDelay = `${i / 50}s`;
    }
  
    const counter = document.querySelector('.counter');
    counter.innerText = target;
  
    const NumberCounter = () => {
      const value = +counter.innerText;
      if (value < target) {
        counter.innerText = Math.ceil(value + 1);
        setTimeout(() => {
          NumberCounter();
        }, 25);
      }
    }
  
    NumberCounter();
  });
  