/*---------------Exercise 1 : Divisible By Three-----------*/
let numbers = [123, 8409, 100053, 333333333, 7]

/*q1 Loop through the array above and determine whether or not each number is divisible by three.*/

/*q2 Each time you loop console.log true or false*/
numbers.forEach(number => {
    if (number % 3 === 0) {
        console.log(`${number} true`)
    }
});


/*---------------Exercise 2 : Attendance---------*/
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
};

/*q1 Prompt the student for their name.*/
let userName = prompt('Please write your name');
let userNameLow = userName.toLocaleLowerCase();
/*q2 If the name is in the object, console.log the name of the student and the country they come from.*/
if (userNameLow in guestList) {
    console.log(`Hi! I'm ${userNameLow}, and I'm from ${guestList[userNameLow]}`)
    /*q3 If the name is not in the object, console.log: "Hi! I'm a guest."*/
} else {
    console.log("Hi! I'm a guest")
};




/*-------------Exercise 3 : Playing With Numbers--------------*/
let age = [20, 5, 12, 43, 98, 55];
let ageSum = (previousValue, currentValue) => previousValue + currentValue;
/*q1 Console.log the sum of all the numbers in the age array.*/
console.log(age.reduce(ageSum));
/*q2 Console.log the highest age in the array.*/
highestAge = 0;

for (i = 0; i < age.length; i++) {
    if (age[i] > highestAge) {
        var highestAge = age[i];
    }
};
console.log(highestAge);