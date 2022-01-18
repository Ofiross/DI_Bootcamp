/*--------------First Part-----------*/

const getRandomInt = (min, max) => {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
}

/*create a function called playTheGame() that takes no parameter.*/
const playTheGame = () => {
    /*start by asking the user if they would like to play the game*/
    let ask = confirm("Would you like to play the game?");
    alert("This is a guessing game where you will have 3 chances to guess the number the computer have picked")
    /*If the answer is false, alert “No problem, Goodbye”.*/
    if (ask === false) {
        return alert("No problem, Goodbye");
    }
    /*If his answer is true, follow these steps:*/
    /*Ask the user to enter a number between 0 and 10*/
    let choice = parseInt(prompt("Please pick a number from 0 - 10"));
    while (isNaN(choice) === true || choice > 10 || choice < 0 || choice == "") {
        alert("You either didn't insert a number or the number you have picked is not between 0 - 10")
        choice = parseInt(prompt("Please pick a number from 0 - 10"));
    }


    /*f the user didn’t enter a number alert
    if (isNaN(choice) === true) {
        return alert("Sorry Not a number, Goodbye")
    /*If the user didn’t enter a number between 0 and 10 alert 
    } else if (choice > 10 || choice < 0) {
        return alert("Sorry it’s not a good number, Goodbye")
    }
    */

    /*create a variable named computerNumber where the value is a random number between 0 and 10 (calling the above function [getRandomInt])*/
    let computerNumber = getRandomInt(1, 10)
    console.log(computerNumber)

    return (test(choice, computerNumber))
}


/*-----------------Second Part--------------*/
const test = (userNumber, computerNumber) => {

    let usVsPc = [
        userNumber > computerNumber,
        userNumber < computerNumber,
        userNumber === computerNumber
    ]

    switch (usVsPc.indexOf(true)) {
        case 0:
            alert("Your number is bigger then the computer’s, guess again");
            choice = parseInt(prompt("Please pick a number from 0 - 10"));
            while (isNaN(choice) === true || choice > 10 || choice < 0 || choice == "") {
                alert("You either didn't insert a number or the number you have picked is not between 0 - 10")
                choice = parseInt(prompt("Please pick a number from 0 - 10"));
            }
            break;
        case 1:
            alert("Your number is smaller then the computer’s, guess again");
            choice = parseInt(prompt("Please pick a number from 0 - 10"));
            while (isNaN(choice) === true || choice > 10 || choice < 0 || choice == "") {
                alert("You either didn't insert a number or the number you have picked is not between 0 - 10")
                choice = parseInt(prompt("Please pick a number from 0 - 10"));
            }
            break;

        case 2:
            return alert("WINNER");
    }

    let usVsPc2 = [
        choice > computerNumber,
        choice < computerNumber,
        choice === computerNumber
    ]

    switch (usVsPc2.indexOf(true)) {
        case 0:
            alert("Your number is bigger then the computer’s, guess again");
            choice = parseInt(prompt("Please pick a number from 0 - 10"));
            while (isNaN(choice) === true || choice > 10 || choice < 0 || choice == "") {
                alert("You either didn't insert a number or the number you have picked is not between 0 - 10")
                choice = parseInt(prompt("Please pick a number from 0 - 10"));
            }
            break;
        case 1:
            alert("Your number is smaller then the computer’s, guess again");
            choice = parseInt(prompt("Please pick a number from 0 - 10"));
            while (isNaN(choice) === true || choice > 10 || choice < 0 || choice == "") {
                alert("You either didn't insert a number or the number you have picked is not between 0 - 10")
                choice = parseInt(prompt("Please pick a number from 0 - 10"));
            }
            break;

        case 2:
            return alert("WINNER");


    }
    return alert("You have run out of chances")
}

