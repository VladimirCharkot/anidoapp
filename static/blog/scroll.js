
window.onscroll = function() {scrollFunction()};

var titular = document.querySelector("#titular");
var titulo = document.querySelector("#titular h1");
var nidito = document.querySelector("#nidito");
var nav = document.querySelector("#nav");
var nav_btn = document.querySelector(".nav_btn");

window.original_titular_fontsize    = titular.style.height;
window.original_titulo_fontsize     = titulo.style.fontSize;
window.original_titulo_transf       = titulo.style.transform;
window.original_nidito_height       = nidito.style.height;
window.original_nidito_width        = nidito.style.width
window.original_nav_height          = nav.style.height;
window.original_btn_fontsize        = nav_btn.style.fontSize;

function scrollFunction() {
    if (document.documentElement.scrollTop < 40){
        titulo.style.transform = window.original_titulo_transf;
        titulo.style.fontSize = window.original_titulo_fontsize;
        titular.style.height = window.original_titular_fontsize;
        
        nidito.style.height = window.original_nidito_height;
        nidito.style.width = window.original_nidito_width;
        
        nav.style.height = window.original_nav_height;
        var btns = document.querySelectorAll(".nav_btn");
        for (i in btns) if (btns[i].style) btns[i].style.fontSize = window.original_btn_fontsize;
    }
    if (document.documentElement.scrollTop > 40) {
        titulo.style.transform = "translateY(0)";
        titulo.style.fontSize = "1rem";
        titular.style.height = "50px";
        nidito.style.height = "0px";
        nidito.style.width = "30px";
        nav.style.height = "0px";
        var btns = document.querySelectorAll(".nav_btn");
        for (i in btns) if (btns[i].style) btns[i].style.fontSize = "0em";
        
    }
}

