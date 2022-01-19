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