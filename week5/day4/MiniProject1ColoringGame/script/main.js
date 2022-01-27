/*--------Mini Project #1 - Coloring Game---------*/
//creating a table with div inside that wi be changed on click to the chosen color
function generate_table() {
    let div = document.getElementsByClassName("maintable")[0];
    for (let i = 0; i < 1705; i++) {
        let canvas = document.createElement('div')
        canvas.setAttribute('class', 'table')
        div.appendChild(canvas)
    };
};
generate_table();

// colors as variables
//1st column
let red = document.getElementsByClassName('red')[0];
red.style.backgroundColor = '#FF0000';
let yellow = document.getElementsByClassName('yellow')[0];
yellow.style.backgroundColor = '#FFFF00';
let green = document.getElementsByClassName('green')[0];
green.style.backgroundColor = '#008000';
let azure = document.getElementsByClassName('azure')[0];
azure.style.backgroundColor = '#87CEFA';
let blue = document.getElementsByClassName('blue')[0];
blue.style.backgroundColor = '#00008B';
let lollipop = document.getElementsByClassName('lollipop')[0];
lollipop.style.backgroundColor = '#EE82EE';
let grey = document.getElementsByClassName('grey')[0];
grey.style.backgroundColor = '#808080';

//2nd column
let orange = document.getElementsByClassName('orange')[0];
orange.style.backgroundColor = '#FF4500';
let olive = document.getElementsByClassName('olive')[0];
olive.style.backgroundColor = '#9ACD32';
let sky = document.getElementsByClassName('sky')[0];
sky.style.backgroundColor = '#40E0D0';
let lightBlue = document.getElementsByClassName('lightBlue')[0];
lightBlue.style.backgroundColor = '#1E90FF';
let purple = document.getElementsByClassName('purple')[0];
purple.style.backgroundColor = '#4B0082';
let pink = document.getElementsByClassName('pink')[0];
pink.style.backgroundColor = '#FFB6C1';
let black = document.getElementsByClassName('black')[0];
black.style.backgroundColor = '#000000';


//3rd column
let papaya = document.getElementsByClassName('papaya')[0];
papaya.style.backgroundColor = '#FFA500';
let mint = document.getElementsByClassName('mint')[0];
mint.style.backgroundColor = '#90EE90';
let cyan = document.getElementsByClassName('cyan')[0];
cyan.style.backgroundColor = '#00FFFF';
let electricBlue = document.getElementsByClassName('electricBlue')[0];
electricBlue.style.background = '#0000FF';
let grape = document.getElementsByClassName('grape')[0];
grape.style.backgroundColor = '#8B008B';
let lightGrey = document.getElementsByClassName('lightGrey')[0];
lightGrey.style.backgroundColor = '#D3D3D3';
let white = document.getElementsByClassName('white')[0];
white.style.backgroundColor = '#FFFFFF';

//create a function that will pick a color base on which one wi have clicked on
let drewingPointer = ''
let getColor = (clr) => {
    drewingPointer = clr.style.backgroundColor;
    console.log(drewingPointer);
};

//changing the "canvas" color to the one we have picked
let canvas = document.getElementsByClassName('table')
for (let i = 0; i < canvas.length; i++) {
    canvas[i].addEventListener('mousedown', e => {
        if (e.target == canvas[i]) {
            canvas[i].style.backgroundColor = `${drewingPointer}`;
        };
        e.preventDefault();
    });
};

//on click on the clear buttn the "canvas" color return to white
function refreshPage() {
    for (let i = 0; i < canvas.length; i++) {
        canvas[i].style.backgroundColor = `white`
    }
};


