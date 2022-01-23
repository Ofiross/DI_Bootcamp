/*-----------------Daily Challenge: 99 Bottles Of Beer--------------*/
const bottlesOfBeer = () => {
    let confirmation = confirm("This is the 99 Bottles Of Beer lyrics creator, woult you like to try it?");

    if (confirmation === false) {
        return "Ok see you around"
    };
    /*---Prompt the user for a number to begin counting down bottles---*/



    let userBottleNum = parseInt(prompt("Please choose a number from 1 - 99 to create the first amount of bottles for the lyrics"));

    let checking = num => [
        num === "",
        isNaN(num),
        num > 99,
        num < 1
    ].some(e => e);


    while (checking(userBottleNum)) {
        alert("you should insert only NUMBER and it can only be between 1 - 99");
        userBottleNum = parseInt(prompt("Please choose a number from 1 - 99 to create the first amount of bottles for the lyrics"));
    };

    /*------variables that will change with every loop----*/

    let bottles = "99";
    let correctNum = bottles - userBottleNum;
    /*---------if statement to check the user number, if it is 1 then we will use it for the bottle that will be passed around, if it is more than 1 then we will use them for being grammatically correct*/

    if (userBottleNum = 1) {
        console.log(`                                       
        ${bottles} bottles of beer on the wall 
        ${bottles} bottles of beer
        Take 1 down, pass it around
        ${correctNum} bottles of beer on the wall`)
    } else {
        console.log(`
        ${correctNum} bottles of beer on the wall
        ${correctNum - userBottleNum} bottles of beer
        Take ${userBottleNum} down, pass them around`)
    }

    /*-------another empty variable for the lyrics----*/
    let lyrics = ''

    /*------a while loop with a condition for terminate the while loop when the condition exists-----*/
    while (correctNum > userBottleNum) {
        userBottleNum = userBottleNum + 1

        lyrics = (`
        ${correctNum} bottles of beer on the wall
        ${correctNum} bottles of beer
        Take ${userBottleNum} down, pass them around
        ${correctNum - userBottleNum} bottles of beer on the wall`)

        console.log(lyrics)

        /*------updating our variables with every loop----*/
        correctNum = correctNum - userBottleNum
    }

    /*------consolo logging the last part when the while loop have met our condition-------*/
    console.log(`
        ${correctNum} bottles of beer on the wall
        ${correctNum - correctNum} bottles of beer
        no bottle of beer on the wall`)
}
bottlesOfBeer()