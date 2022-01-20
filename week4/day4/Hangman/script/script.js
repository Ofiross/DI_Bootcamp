/*---------Create A Hangman Game---------*/
const hangmanGame = () => {
    let likeToPlay = confirm("this is an Hangman game, would you like to continue?")
    if (confirm === false) {
        return alert("Thank you and see you next time.")
    }

    let chosenWord = prompt("please choose a word contain minimum 8 letters").toUpperCase();
    while (chosenWord == "" || chosenWord.length < 8 || isNaN(chosenWord) === false || chosenWord == null || (!/^[a-zA-Z]+$/.test(chosenWord))) {
        alert("you inserted wrong option, please try again");
        chosenWord = prompt("Please pick one letter").toUpperCase();
    }
    let word = chosenWord.split("");

    let answerstars = []
    for (var i = 0; i < chosenWord.length; i++) {
        answerstars[i] = "*";
    }

    let remainingChar = chosenWord.length;
    let guesses = [];
    let tries = 10

    while (tries > 0) {
        let player2Guess = prompt("Please pick one letter").toUpperCase();
        while (guesses.includes(player2Guess) === true || player2Guess == "" || player2Guess.length > 1 || isNaN(player2Guess) === false || player2Guess == null || (!/^[a-zA-Z]+$/.test(player2Guess))) {
            alert("you inserted wrong option, please try again");
            player2Guess = prompt("Please pick one letter").toUpperCase();
        }

        for (var j = 0; j < word.length; j++) {
            if (word[j] === player2Guess) {
                answerstars[j] = player2Guess;
                remainingChar--;
                console.log(remainingChar)
                guesses.push(player2Guess)
                console.log(answerstars.toString());

            }
        }
        tries = tries - 1
        console.log(`The letters that you have used until now are ${guesses}`)
    }
    if (tries = 0) {
        return `YOU LOSE, The answer was ${chosenWord}`
    } else {
        console.log("CONGRATS YOU WIN")
    }
}
