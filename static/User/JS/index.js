
function hamburgerOn(){

        var x = document.getElementById("navbarNav");
        if (x.style.display === "none") {
          x.style.display = "block";
        } else {
          x.style.display = "none";
        }
      
}

function hamburgerOff(){

        var x = document.getElementById("navbarNav");
        if (x.style.display === "none") {
          x.style.display = "block";
        } else {
          x.style.display = "none";
        }
      
}


// NavBar Color Change When Page Scroll
// JS-1 : NavBar Color Change When Page Scroll
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
    document.getElementById("Navbar").style.backgroundColor =
      "rgba(0, 0, 0, 0.9)";
    document.getElementById("Navbar").style.transition = "0.3s";
  } else {
    document.getElementById("Navbar").style.backgroundColor = "transparent";
  }
}

// Change Input Value When Slider Slides And Change Value of Slider When We Enter Input
// JS-1 : Change Input Value When Slider Slides And Change Value of Slider When We Enter Input

var Slider = document.getElementById("range-slider");
var PriceInput = document.getElementById("price-value-input");

function sliderInput() {
  Slider.value = PriceInput.value;
}

PriceInput.addEventListener("input", sliderInput);

function updateInput() {
  PriceInput.value = Slider.value;
}

Slider.addEventListener("input", updateInput);

// JS-1 : it clicks the submit button when user press enter in input field
var ipOnSubmit = document.getElementById("price-value-input");
ipOnSubmit.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("budget-apply-btn").click();
  }
});
