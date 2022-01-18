const playTheGame = () => {
    let ask = confirm("Would you like to play the game?");
    if (ask === false) {
        return alert("No problem, Goodbye");
    }
    let choice = prompt("Please pick a number from 0 - 10");
}
