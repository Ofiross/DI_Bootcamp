/*---------------Exercise 1 Favorite Color-----------------*/

let me = ["my", "favorite", "color", "is", "blue"];

console.log(me.join(' '));


/*---------------Exercise 2  Mixup-----------------*/

/*q1*/

let str1 = "developers";

let str2 = "institute";

/*q2*/

str1New = str2.slice(0, 2).concat(str1.slice(2,));
str2New = str1.slice(0, 2).concat(str2.slice(2,));

/*q3*/

let newWord = str1New.concat(' ', str2New);

/*q4*/
console.log(newWord);


/*----------------Exercise 3 : Calculator---------------*/
alert(`This is a calculator, please insert two numbers to check their sum`);

var x = prompt('please inseret first number');
var num1 = parseInt(x);

var y = prompt('please inseret first number');
var num2 = parseInt(y);

alert(`The sum of your numbers is ${num1 + num2}`);