/*----Exercise XP---*/
/*---Exercise 2 : Work With Forms---*/

//1. Retrieve the form and console.log it.
let form = document.querySelector('form');
console.log(form);

//2. Retrieve the inputs by their id and console.log them.
let fstName = document.getElementById('fname')
console.log(fstName);
let lstName = document.getElementById('lname')
console.log(lstName);

//3. Retrieve the inputs by their name attribute and console.log them.
console.log(document.getElementsByName('fname')[0]);
console.log(document.getElementsByName('lname')[0]);

//4. When the user submits the form (ie. submit event listener) get the values of the input tags, make sure that they are not empty, create an li per input value,then append them to a the <ul class="usersAnswer"></ul>, below the form.

function makeLst() {
    let ulList = document.getElementsByClassName('usersAnswer')[0];
    ulList.innerHTML = "";
    let firstName = document.getElementById("fname");
    let lastName = document.getElementById("lname");
    let arr = [firstName, lastName]

    arr.forEach(txt => {
        let li = document.createElement('li');
        li.textContent = txt.value;
        ulList.appendChild(li)
    })
    fstName.value = "";
    lstName.value = "";
}

form.addEventListener("submit", function (e) {
    e.preventDefault();
    makeLst();
});



