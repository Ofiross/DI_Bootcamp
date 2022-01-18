const playTheGame = () => {
    let ask = confirm("Would you like to play the game?");
    if (ask === false) {
        return alert("No problem, Goodbye");
    }
    let choice = prompt("Please pick a number from 0 - 10");
    if (isNaN(choice) === true) {
        return alert("Sorry Not a number, Goodbye")
    } else if (choice > 10 || choice < 0) {
        return alert("Sorry it’s not a good number, Goodbye")
    }
}
