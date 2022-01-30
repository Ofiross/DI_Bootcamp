/**********************Ex1*************************/


let ani = document.getElementById('animate')
let position = 0;
let movementSpeed = 1
let spaceToMove = 350
let myMove = () => {
    setInterval(function () {
        ani.style.left = (position += movementSpeed) + "px";
        if (position <= 0 || position >= 350) {
            movementSpeed *= -1;
        }
    }, 1000 / 60);
};


/**********************Ex2*************************/
/* let smallsq = document.getElementById("box");
let targetsq = document.getElementById("biggerBox");

smallsq.addEventListener("dragstart", dragStart);

let dragStart = (e) => {
    e.dataTransfer.setData("text", e.target.id);
};



targetsq.addEventListener("dragover", dragOver);
targetsq.addEventListener("drop", drop);
targetsq.addEventListener("dragenter", dragEnter);
targetsq.addEventListener("dragleave", dragLeave);


let dragOver = (e) => {
    e.preventDefault();
};

let drop = (e) => {
    e.preventDefault();
    let dataSquare = e.dataTransfer.getData("text");
    let box = document.getElementById(dataSquare);
    e.target.appendChild(box);
};

let dragEnter = (e) => {
    e.target.style.backgroundColor = "green"
    e.target.classList.add('over');
};

function dragLeave(e) {
    e.target.style.backgroundColor = "lightblue"
    e.target.classList.remove('over');
};
 */

let square = document.getElementById('box');
square.addEventListener("dragstart", function (event) {
    console.log("drag " + "X: " + event.clientX + " Y: " + event.clientY);
});

square.addEventListener("dragend", function (event) {
    let _x = event.clientX;
    let _y = event.clientY;
    event.target.style.left = _x + "px";
    event.target.style.top = _y + "px";
    event.target.style.position = "absolute";
});
