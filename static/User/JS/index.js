
// NavBar Color Change When Page Scroll 
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if(document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
        document.getElementById("Navbar").style.backgroundColor = "rgba(0, 0, 0, 0.9)";
        document.getElementById("Navbar").style.transition = "0.3s"
    }
    else {
        document.getElementById("Navbar").style.backgroundColor = "transparent";
    }
}





// Change Input Value When Slider Slides And Change Value of Slider When We Enter Input

var Slider = document.getElementById("range-slider");
var PriceInput = document.getElementById("price-value-input");

function sliderInput(){
    Slider.value = PriceInput.value;
}

PriceInput.addEventListener("input",sliderInput);


function updateInput(){
    PriceInput.value = Slider.value;
}

Slider.addEventListener("input",updateInput);
