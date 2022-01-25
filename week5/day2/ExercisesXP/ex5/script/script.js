/*----Bonus Exercise 5 : Event Listeners----*/

//Add as many events listeners as possible to one element on your webpage. Each listener should do a different thing, for instance- change position x, change position y, change color, change the font size… and more.

let shape = document.getElementById('shape');

let changeToSquare = sqr => sqr.target.style.borderRadius = "0";
shape.addEventListener("mouseover", changeToSquare);

let backToRound = rnd => rnd.target.style.borderRadius = "50%";
shape.addEventListener("mouseout", backToRound);

let textCng = text => text.target.style.fontWeight = `bold`;
shape.addEventListener('click', textCng);

let move = mv => mv.target.style.left = "200px";
shape.addEventListener('click', move);

let p = document.getElementById('whoAmI');

let textSize = sz => sz.target.style.fontSize = `${Math.floor(Math.random() * 50)}px`;
p.addEventListener('click', textSize);

let color = cl => cl.target.style.color = "blue"
p.addEventListener('mouseover', color);

let colorrtn = clr => clr.target.style.color = "white"
p.addEventListener('mouseout', colorrtn);


