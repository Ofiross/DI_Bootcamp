/*-------Exercises XP Gold-------*/

/*----Exercise 1 : Select A Kind Of Music----*/
//1. Display the value of the selected option.
let slct = document.getElementById('genres');
let val = slct.options[slct.selectedIndex].value;
console.log(val);


//2. Add an additional option to the select tag:<option value="classic">Classic</option>
let newOptn = document.createElement('option');
let optionText = document.createTextNode('Classic');
newOptn.appendChild(optionText);
newOptn.setAttribute('value', 'classic');
slct.appendChild(newOptn);

//3. slct.appendChild(newOptn);
slct.options[slct.selectedIndex].defaultSelected = false;
newOptn.defaultSelected = true;




/*----------Exercise 2: Delete Colors---------*/
//3. Add a click event listener to the <input type="button">. When clicked on, it should call a function named : removecolor() that removes the selected color from the dropdown list.

let form = document.querySelector('form')[0];

let removeSelected = function () {
    let slct = document.getElementById('colorSelect');
    slct.remove(slct.selectedIndex);
}
let btn = document.getElementsByTagName('input')[0];
btn.addEventListener('click', removeSelected);
