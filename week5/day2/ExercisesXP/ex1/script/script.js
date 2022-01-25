/*Exercises XP*/
/*Exercise 1 : Change The Article*/

//1. Using a DOM property, retrieve the h1 and console.log it.
let h1 = document.querySelector('h1');
console.log(h1);

//2. Using DOM methods, remove the last paragraph in the <article> tag.
let art = document.querySelector('article');
art.lastElementChild.remove();

//3. Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
let h2 = document.querySelector('h2');
let changeBackground = (e) => e.target.style.background = "red";
h2.addEventListener("click", changeBackground);

//3. Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
let h3 = document.querySelector('h3');
let hideText = (text) => text.target.style.display = "none";
h3.addEventListener("click", hideText);

//4. Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
let btn = document.createElement('button');
btn.innerHTML = 'click to make paragraphs bold';
btn.setAttribute('id', 'btn');
art.appendChild(btn);
let p = document.querySelectorAll('p');
let par = () => {
    for (let i = 0; i < p.length; i++) {
        p[i].style.fontWeight = 'bold'
    };
};
btn.onclick = par;

//6. BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100
let textSizeChange = (size) => size.target.style.fontSize = `${Math.floor(Math.random() * 100)}px`;

h1.addEventListener("mouseover", textSizeChange);

//7. BONUS : When you hover on the 2nd paragraph, it should fade out



let fade = (fd) => {
    fd.target.style.opacity = .5;
};

let unfade = (unfd) => {
    unfd.target.style.opacity = 1;
};
h2.addEventListener("mouseover", fade);
h2.addEventListener("mouseout", unfade)
