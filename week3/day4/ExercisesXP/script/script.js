/*------------Exercise 1: Simple If/Else Statement-------------*/

/*q1*/
let x = 30;
let y = 20;

/*q2*/
if (x > y) {
    console.log(`The bigger Number is ${x}`)
};


/*-----------Exercise 2: Chihuahua------------*/

/*q1*/
let newDog = "Chihuahua";

/*q2*/
let letterAmount = newDog.length;
console.log(`the amount of character in newDog is ${letterAmount}`);

/*q3*/
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

/*q4*/
if (newDog = "Chihuahua") {
    console.log(`I love Chihuahuas, it’s my favorite dog breed`)
} else {
    console.log(`I dont care, I prefer cats`)
};


/*-----------------Exercise 3: Even Or Odd----------------*/

/*q1*/
let userChoice = prompt(`Please inset a number: `)

/*q2*/
if (userChoice % 2 == 0) {
    alert(`${userChoice} is an even number`)
} else {
    alert(`${userChoice} is an odd number`)
};


/*---------Exercise 4: Group Chat-----------*/

/*q1*/
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let usersNumber = users.slice(2).length;

let onlineUsers = [
    users.length > 2,
    users.length === 2 && users.length > 1,
    users.length === 1
];

switch (onlineUsers.indexOf(true)) {
    case 0:
        console.log(`${users[0]} and ${users[1]} are online and there are other ${usersNumber} additional users online right now`)
        break;
    case 1:
        console.log(`${users[0]} and ${users[1]} are online`)
        break;
    case 2:
        console.log(`${users} is online`)
        break;
    default:
        console.log(`no one is online`)
        break;

};