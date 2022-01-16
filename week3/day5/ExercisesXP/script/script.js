/*-------------------Exercise 1 : List Of People-------------------*/
/*--Part I - Review About Arrays--*/
let people = ["Greg", "Mary", "Devon", "James"];

/*q1Write code to remove “Greg” from the people array.*/
people.shift();

/*q2 Write code to replace “James” to “Jason”.*/
people.splice(2, 1, 'Jason');

/*q3 Write code to add your name to the end of the people array.*/
people.push('Ofir')

/*q4 Write code that console.logs Mary’s index.*/
console.log(people.indexOf('Mary'));

/* q5 Write code to make a copy of the people array using the slice method.*/
let peopleCopy = people.slice(1, -1);

/*q6 Write code that gives the index of “Foo”.*/
console.log(people.indexOf('Foo')); /*The result is -1 as the name Foo doesn't make a part of the current string and for that reason the return is a negative one as it is not in the string.

/*q7 Create a variable called last which value is the last element of the array.*/

let last = people.splice(-1);


/*--Part II - Loops--*/

/*q1 Using a loop, iterate through the people array and console.log each person.*/
people.forEach(person => console.log(person));

/*q2 Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .*/

for (i = 0; i < people.length; i++) {
    if (people[i] === 'Jason') { break; }
    console.log(people[i]);
};



/*----------Exercise 2 : Your Favorite Colors-----------*/

/*q1 Create an array called colors where the value is a list of your five favorite colors.*/

let colors = ['blue', 'grey', 'black', 'beige'];
let numbers = ['1st', '2nd', '3rd', '4th'];
/*q2 Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… */

colors.forEach((colors, choice) => {
    const choiceRanking = numbers[choice];
    console.log(`My ${choiceRanking} color of choice is: ${colors}`);
});


/*-------------Exercise 3 : Repeat The Question------------*/

/*q1 Prompt the user for a number.*/
/*q2 While the number is smaller than 10 continue asking the user for a new number.*/

let userNumberChoice = prompt('Please choose a number bigger than 10');
while (userNumberChoice < 10) {
    alert("Please enter a number bigger than 10");
    userNumberChoice = prompt("What's your correct number of choice?");
};



/*------------Exercise 4 : Building Management------------*/

/*q1 Copy and paste this object to your Javascript file.*/
let building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}

/*q2 Console.log the number of floors in the building.*/
console.log(`there are ${building.numberOfFloors} floors in the building`);

/*q3 Console.log how many apartments are on the floors 1 and 3.*/
console.log(` on the first floor there are ${building.numberOfAptByFloor.firstFloor} and on the third floor there are ${building.numberOfAptByFloor.thirdFloor}`);

/*q4 Console.log the name of the second tenant and the number of rooms he has in his apartment.
*/
console.log(`the second tenant name is ${building.nameOfTenants[1]} and he has ${building.numberOfRoomsAndRent.dan[0]} rooms in is apartment`);

/*q5 Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.*/

if ((building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200
};


/*---------------Exercise 5 : Family-----------------*/

/*q1 Create an object called family with a few key value pairs.
*/

let family = {
    father: "Jhon",
    mother: "Sarah",
    son: "Liam"
};

/*q2 Using a for loop, console.log the keys of the object.*/
for (let familyMember in family) {
    console.log(familyMember)
};

/*q3 Using a for loop, console.log the values of the object.*/
for (let familyMember in family) {
    const nameOfMember = family[familyMember];
    console.log(nameOfMember)
};



/*---------Exercise 6------------*/
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
};

/*q1 Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”*/
arr = [];
for (let prop in details) {
    arr.push(" " + prop + " " + details[prop])
}
console.log(arr.join(" "));


/*------------Exercise 7 : Secret Group-----------*/

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]

/*q1 A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.*/
/*q2 Console.log the name of their secret society. The output should be “ABJKPS”*/
arr = []
names.forEach(name => {
    arr.push(name.charAt(0));
});
console.log(arr.join(""));
