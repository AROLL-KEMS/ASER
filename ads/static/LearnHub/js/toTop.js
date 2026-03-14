document.addEventListener("DOMContentLoaded", function () {
    const mybutton = document.getElementById("btn-back-to-top");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 100) {
            mybutton.style.display = "block";
        } else {
            mybutton.style.display = "none";
        }
    });

    mybutton.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
});