/*----------Exercise 1 : Information---------*/

/*
Part I : function with no parameters

1. Create a function called infoAboutMe() that takes no parameter.
2. The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
3. Call the function.*/

let infoAboutMe = () => {
    console.log("My name is Ofir, I am 32 years old, like sports and technology")
};
infoAboutMe();

/*
Part II : function with three parameters

1. Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
2. The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
3. Call the function twice with the following arguments:*/

let infoAboutPerson = (personName, personAge, personFavoriteColor) => {
    console.log(`Your Name is ${personName}, you are ${personAge} and your favorite color is ${personFavoriteColor}`)
};
infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");



/*------------Exercise 2 : Tips-----------*/

/*John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

1. Create a function named calculateTip() that takes no parameter.
2. Inside the function, ask John for the amount of the bill.
3.Here are the rules
If the bill is less than $50, tip 20%.
If the bill is between $50 and $200, tip 15%.
If the bill is more than $200, tip 10%.

4. Console.log the tip amount and the final bill (bill + tip).
5. Call the calculateTip() function.*/

let calculateTip = () => {
    let bill = parseInt(prompt('Please insert bill total amount'));
    let tip = 0;
    if (bill < 50) {
        tip = bill * 1.2
    } else if (bill > 50 && bill < 200) {
        tip = bill * 1.15
    } else {
        tip = bill * 1.1
    }
    return (` you should leave an amout of ${tip} as an onest tip`)
};
calculateTip();


/*----------------Exercise 3 : Find The Numbers Divisible By 23----------------*/

/*
1. Create a function call isDivisible() that takes no parameter.
2. In the function, loop through numbers 0 to 500.
3. Console.log all the numbers divisible by 23.
4. At the end, console.log the sum of all numbers that are divisible by 23.*/
let isDivisible = () => {
    let divisible = [];
    const reducer = (previousV, currentV) => previousV + currentV;
    for (let i = 1; i <= 500; i++) {
        if (i % 23 === 0) {
            divisible.push(i);
        }
    }
    console.log(`the array sum is ${divisible.reduce(reducer)}`)
    return divisible
}

isDivisible();

/*5. Bonus: Add a parameter divisor to the function.*/
let isDivisible2 = (divisor) => {
    let divisible = [];
    const reducer = (previousV, currentV) => previousV + currentV;
    for (let i = divisor; i <= 500; i++) {
        if (i % divisor === 0) {
            divisible.push(i)
        }
    }
    console.log(`the array sum is ${divisible.reduce(reducer, divisor)}`)
    return divisible
}
isDivisible2();


/*-------------Exercise 4 : Shopping List---------------*/
/*1. Add the stock and prices objects to your js file.*/
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
};

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
};

/*2. Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.*/
let shoppingList = ['banana', 'orange', 'apple'];


/*3. Create a function called myBill() that takes no parameters.*/

let myBill = () => {
    /*4. The function should return the total price of your shoppingList. In order to do this you must follow these rules:
    The item must be in stock.
    If the item is in stock find out the price in the prices object.*/
    totalPrice = 0;
    for (let i = 0; i < shoppingList.length; i++) {
        if (stock[shoppingList[i]] > 0) {
            totalPrice += prices[shoppingList[i]]
            /*6. Bonus: If the item is in stock, decrease the item’s stock by 1*/
            stock[shoppingList[i]] -= 1;
        }
    }
    return totalPrice
};
/* .5 Call the myBill() function.*/
myBill();



/*---------------Exercise 5 : What’s In My Wallet ?------------------*/

let changeEnough = (itemPrice, amountOfChange) => {
    /* creating an empty array to push inside calculated amount*/
    change = [];
    for (let i = 0; i < 1; i++) {
        /*calculating each number to change it to quarters, dimes, nickel, penny */
        change.push(amountOfChange[0] * .25, amountOfChange[1] * .1, amountOfChange[2] * .05, amountOfChange[3] * .01)
        /*sum all the change we have in the array*/
        const reducer = (previousValue, currentValue) => previousValue + currentValue;
        totalChange = change.reduce(reducer);
        /*check if the sum of our change is higher or lower than the item price*/
        if (itemPrice < totalChange) {
            return true
        } else
            return false
    }
};



/*-----------------Exercise 6 : Vacations Costs---------------------*/

/*1. Define a function called hotelCost()*/

let hotelCost = () => {
    let numberOfNights = prompt('Please indicate the amout of nights you would like to book your room for')
    while (numberOfNights.length === 0) {
        alert('You didnt inserted any number of nights for your booking!')
        numberOfNights = prompt('Please indicate the amout of nights you would like to book your room for')
    };
    let totalForNights = numberOfNights * 140

};
hotelCost();


/*q2 Define a function called planeRideCost()*/

let planeRideCost = () => {
    let destinations = {
        London: 183,
        Paris: 220,
        Rome: 400
    };
    let destination = prompt('Please indicate the destination for your vacation using alphabetical only')
    while (destination == "" || isNaN(destination) === false || destination == null || (!/^[a-zA-Z]+$/.test(destination))) {
        alert('Please check the information you have entered and try again')
        destination = prompt('Please indicate the destination for your vacation using alphabetical only')
    }
    let upperCase = destination.charAt(0).toUpperCase() + destination.slice(1);
    if (upperCase in destinations) {
        let TotalTickes = destinations[upperCase]

    } else {
        let TotalTickes = 300

    }
};
planeRideCost();

/*3 .Define a function called rentalCarCost().*/
let rentalCarCost = () => {
    let carRental = +prompt('For how many days would you like to rent a car?')
    while (isNaN(carRental) == true) {
        alert('you didnt inserted any number of days for your rental period!')
        carRental = +prompt('For how many days would you like to rent a car?')
    };
    if (carRental > 10) {
        let totalCar = carRental * 38

    } else {
        let totalCar = carRental * 40

    }
};
rentalCarCost();


/*4. Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.*/

let totalVacationCost = () => {
    console.log(`the total car price will be${rentalCarCost()} the total plane tickets price will be ${planeRideCost()} and the total price for hotel staying will be${hotelCost()}`)
}
totalVacationCost();