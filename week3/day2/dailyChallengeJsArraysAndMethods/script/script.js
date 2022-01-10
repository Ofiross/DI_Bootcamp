/*---------------Exercise 1:-----------------*/

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift();

fruits.sort();

fruits.push("Kiwi");

fruits.shift("Apples");

fruits.reverse();



/*--------------Exercise 2:---------------*/
let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(moreFruits[1][1][0])