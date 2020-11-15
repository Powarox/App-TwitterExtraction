"use strict";


let btnTrump = document.getElementById("btnTrump");
let btnBiden = document.getElementById("btnBiden");

let trump = document.querySelector(".trump");
let biden = document.querySelector(".biden");

let legend = document.querySelector("h2");


btnTrump.addEventListener('click', function(e){
    if(getComputedStyle(trump).display != "none"){
        trump.style.display = "none";
        legend.style.display = "none";
    }
    else{
        biden.style.display = "none";
        trump.style.display = "grid";
        legend.style.display = "flex";
    }
})

btnBiden.addEventListener('click', function(e){
    if(getComputedStyle(biden).display != "none"){
        biden.style.display = "none";
        legend.style.display = "none";
    }
    else{
        trump.style.display = "none";
        biden.style.display = "grid";
        legend.style.display = "flex";
    }
})
