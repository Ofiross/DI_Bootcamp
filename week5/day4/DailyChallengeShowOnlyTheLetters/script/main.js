function allLetter(inputtxt) {
    var letters = /[A-Za-z]/;
    if (inputtxt.value.match(letters)) {
        alert('Your name have accepted : you can try another');
        return true;
    }
    else {
        alert('Please input alphabet characters only');
        return false;
    }
}

let text = document.getElementById('textfield');
let form = document.getElementById('form');

form.addEventListener('submit', function (e) {
    e.preventDefault();
    allLetter(text);
});
