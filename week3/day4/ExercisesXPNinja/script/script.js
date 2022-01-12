/*-------------Exercise 1 : Age Difference-------------*/

/*q1 Given the years two people were born, find the date when the younger one is exactly half the age of the older.
Notes: The dates are given in the format YYYY*/

alert("Lets find out the date when a younger person is half the age of an older person");

let firstPersonBirth = prompt("Please enter the younger person birth date Month/Day/Year");

let secondPersonBirth = prompt("Please enter the older person birth date Month/Day/Year");

let firstPersonBirthAsDate = new Date(firstPersonBirth);

let secondPersonBirthAsDate = new Date(secondPersonBirth);

let firstPersonBirthAsNumber = Date.parse(firstPersonBirthAsDate);

let secondPersonBirthAsNumber = Date.parse(secondPersonBirthAsDate);

let differenceInAge = firstPersonBirthAsNumber - secondPersonBirthAsNumber;

let halfDateAsNumber = differenceInAge + firstPersonBirthAsNumber;

let result = new Date(halfDateAsNumber);

alert(`The date when the younger person will be half the age of the older person is ${result}`)



/*-----------------Exercise 2 : Zip Codes--------------*/

/*q1 While working in a Post Office you must have the clients’ zip code in order to send them their letters*/

let clientZipCode = prompt("Please enter your zip code here");
while (clientZipCode.length !== 5 || isNaN(clientZipCode) == true) {
    alert("Please enter your zip code!");
    clientZipCode = prompt("What's your zip code");
};


/*-----------Exercise 3 : Secret Word------------*/

let userInput = prompt("Please write a word of your choice in here");
let toLowerCase = userInput.toLocaleLowerCase();

let noVowels = toLowerCase.replace(/a|e|i|o|u/g, "@");
console.log(noVowels);
alert(noVowels);