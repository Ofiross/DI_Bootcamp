/*---------------Exercise 1 : Evaluation-----------------*/

5 >= 1 /*true*/
0 === 1 /*false*/
4 <= 1 /*false*/
1 != 1 /*false*/
"A" > "B" /*false*/
"B" < "C" /*true*/
"a" > "A" /*true*/
"b" < "A" /*false*/
true === false /*false*/
true != true /*false*/


/*-----------Exercise 2 : Ask For Numbers---------*/
let x = prompt('please write down any 2 numbers separated by commas to find thier sum');

let y = x.split(',').map(Number);
let arr = y.map(Number);

arr.reduce((a, b) => a + b, 0);


/*-------------Exercise 3 : Find Nemo-------------*/
let findingNemo = prompt(`Please write a sentence with the word Nemo`);
let wordToFind = "Nemo";

if (findingNemo.includes("Nemo")) {
    let position = findingNemo.search("Nemo");
    console.log(`I found Nemo at ${position}`);
} else {
    console.log("I can’t find Nemo");
}


/*---------------Exercise 4 : Boom-------------*/

let userNumber = parseInt(prompt("Please insert a number"));

let userNumberOfChoice = [
    userNumber < 2,
    userNumber % 2 === 0 && userNumber > 2 && userNumber % 5 == 0,
    userNumber % 2 === 0 && userNumber > 2,
    userNumber > 2,
    userNumber % 2 === 0
];

switch (userNumberOfChoice.indexOf(true)) {
    case 0:
        result = ("boom");
        console.log(result);
        break
    case 1:
        result = (("b" + ("o".repeat(userNumber) + 'm' + '!')));
        console.log(result.toUpperCase());
        break
    case 2:
        result = (("b" + ("o".repeat(userNumber) + 'm' + '!')));
        console.log(result);
        break
    case 3:
        result = (("b" + ("o".repeat(userNumber) + 'm')));
        console.log(result);
        break
    case 4:
        result = ("boom" + "!")
        console.log(result);
        break
};