/*------Exercises XP--------*/



/*----------Exercise 1 : Change The Navbar-------*/
/*1. In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.*/
document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation");


/*2. We are going to add a new <li> to the <ul>.
-First, create a new <li> tag (use the createElement method).
-Create a new text node with “Logout” as its specified text.
-Append the text node to the newly created list node (li).
-Finally, append this updated list node to the unordered list above, using the appendChild method.-*/

const l = document.createElement('li');
const log = document.createTextNode("Logout");
l.appendChild(log);
document.getElementsByTagName("ul")[0].setAttribute("id", "menu")
menu.appendChild(l)
console.log(menu.firstElementChild.textContent);
console.log(menu.lastElementChild.textContent);

/*--------Exercise 2 : Users--------*/


/*1. change the name “Pete” to “Richard”.*/
document.getElementsByClassName("list")[0].getElementsByTagName('li')[1].textContent = "Richard";

/*2. Change each first name of the two <ul>'s to your name.*/
let nameLists = document.getElementsByClassName("list");
nameLists[0].getElementsByTagName('li')[0].textContent = "Ofir";
nameLists[1].getElementsByTagName('li')[0].textContent = "Ofir";

/*3. At the end of each <ul> add a <li> that says “Hey students”.*/
let li = document.createElement('li');
let greet = document.createTextNode("Hey students");
li.appendChild(greet)
nameLists[0].appendChild(li)

let lis = document.createElement('li');
let greet2 = document.createTextNode("Hey students");
lis.appendChild(greet2)
nameLists[1].appendChild(lis)

/*4. Delete the name Sarah from the second <ul>.*/
const s = nameLists[1].getElementsByTagName('li')[1]
s.parentElement.removeChild(s)

/*Bonus
Add a class called student_list to both of the <ul>'s.
Add the classes university and attendance to the first <ul>.*/
nameLists[0].classList.add("student_list", "university", "attendance");
nameLists[1].classList.add("student_list");


/*-----Exercise 3 : Users And Style-----*/

/*1. Add a “light blue” background color and some padding to the <div>.*/
document.getElementsByTagName("div")[2].classList.add("thirdDiv")
document.getElementsByClassName("thirdDiv")[0].style.background = "lightblue";
document.getElementsByClassName("thirdDiv")[0].style.padding = "20px";

/*2. Do not display the first name (John) in the list.*/
document.body.getElementsByTagName('ul')[3].classList.add("forthul")
document.getElementsByClassName("forthul")[0].getElementsByTagName("li")[0].hidden = true;

/*3. Add a border to the second name (Pete).*/
document.getElementsByClassName("forthul")[0].getElementsByTagName("li")[1].style.border = "1px solid black"

/*4. Change the font size of the whole body.*/
document.body.style.fontSize = "20px"


/*5. Bonus If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).*/
/*I did not greet Jhon as well as we made him Hidden but if he wasnt the process was the same with a diffrent index to the first user*/
let thirdDiv = document.getElementsByClassName("thirdDiv")[0].style;
let colorDiv = thirdDiv.getPropertyValue('background');
if (colorDiv === "lightblue") {
    alert(`Hello ${document.getElementsByClassName("forthul")[0].getElementsByTagName("li")[1].textContent}`)
}