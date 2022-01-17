/*----------Exercise 1: Random Number-----------*/
/*1. Get a random number between 1 and 100.
2. Console.log all even numbers from 0 to the random number.*/

let isEven = (num) => {
    for (let i = 1; i <= num; i++) {
        if (i % 2 === 0) {
            console.log(i)
        }
    }
};


/*----------Exercise 2: Capitalized Letters--------*/
/*1. Create a function that takes a string as an argument.
Have the function return:
The string but all letters in even indexes should be capitalized.
The string but all letters in odd indexes should be capitalized.*/

let capitalize = (string) => {
    let evenOddIndex = "";
    for (let i = 0; i < string.length; i++) {
        if (i % 2 === 0) {
            evenOddIndex += string[i].toUpperCase();
        } else {
            evenOddIndex += string[i].toLowerCase();
        }
    }
    return evenOddIndex
};



/*-------------Exercise 3 : Is Palindrome?----------*/
/*long way*/
let wordBackwards = (str) => {
    let checkMeBckwards = ""
    for (let i = str.length - 1; i >= 0; i--) {
        checkMeBckwards += str[i]
    }
    return checkMeBckwards;
};

let isPalindrome = (str) => {
    result = ""
    strBackwards = wordBackwards(str);
    if (strBackwards === str) {
        result = "The word is palindrome";
    } else {
        result = "The word is NOT a palindrome";
    }
    return result
};


/*shorter way*/
let checkPalindrome = (str) => {
    return str == str.split('').reverse().join('');
};


/*-----------Exercise 4 : Biggest Number--------------*/

let biggestNumberInArray = (arr) => {
    let biggest = 0;
    for (let i = 0; i <= arr.length; i++) {
        if (arr[i] > biggest) {
            biggest = arr[i];
        }
    }
    return biggest
};


/*--------------Exercise 5: Unique Elements------------*/
let filteredLst = (list) => {
    newLst = list.filter((e, i, a) => a.indexOf(e) === i);
    return newLst
};
