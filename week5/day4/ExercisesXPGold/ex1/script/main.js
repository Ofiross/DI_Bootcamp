/**************Exercises XP Gold  Exercise 1 : Animation With The Alphabet****************/

//1. Create multiple squares/boxes with letters inside. There should be 26 squares/boxes for all the letters (A to Z) next to each other.
//2. Make all the squares draggable.
//3. You should be able to drag and drop the letters depending on their coordinates x and y.

document.querySelector('div').addEventListener("dragend", function (event) {
    let _x = event.clientX;
    let _y = event.clientY;
    event.target.style.left = _x + "px";
    event.target.style.top = _y + "px";
    event.target.style.position = "absolute";
});
