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
