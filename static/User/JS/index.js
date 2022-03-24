
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



// Get Value Of Slider 
// https://www.youtube.com/watch?v=FShnKqPXknI
const SliderInput = document.querySelectorAll(".budget-slider input");
PriceInput = document.querySelectorAll("budget-input input");

SliderInput.forEach(input => {
    input.addEventListener("input", e => {
        let SliderVal = parseInt(SliderInput[0].value);
        // console.log(SliderVal);

        PriceInput.value = SliderVal;

    });


})
