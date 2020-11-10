"use strict";


let btnTrump = document.getElementById("btnTrump");
let btnBiden = document.getElementById("btnBiden");

let trump = document.querySelector(".trump");
let biden = document.querySelector(".biden");


btnTrump.addEventListener('click', function(e){
    if(getComputedStyle(trump).display != "none"){
        trump.style.display = "none";
    } 
    else{
        biden.style.display = "none";
        trump.style.display = "grid";
        trump.style.grid.template.column = "1fr 1fr";
    }
})

btnBiden.addEventListener('click', function(e){
    if(getComputedStyle(biden).display != "none"){
        biden.style.display = "none";
    } 
    else{
        trump.style.display = "none";
        biden.style.display = "grid";
        biden.style.grid.template.column = "1fr 1fr";
    }
})

