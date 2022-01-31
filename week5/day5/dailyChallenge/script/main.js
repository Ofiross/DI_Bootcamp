let pattern = [0, 0, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0];


for (let i = 0; i < 49; i++) {
    canvas = document.createElement("div");
    canvas.setAttribute("class", "canvas");
    document.getElementById("table").appendChild(canvas);
    let star = document.createTextNode('*');
    if (pattern[i])
        canvas.appendChild(star)
};