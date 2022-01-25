/*-------Exercises XP Ninja -------*/
//Exercise 2 : Validate The Email
let form = document.getElementById('emailForm');

let mail = document.getElementById('email')

function ValidateEmail() {

    let contain = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if (mail.value.match(contain)) {
        alert("Valid email address!");
        document.mailform.email.focus();
        return true;

    } else {
        alert("Invalid email address!");
        document.mailform.email.focus();
        return false;
    }
}

form.addEventListener("submit", function (e) {
    e.preventDefault();
    ValidateEmail();
});



