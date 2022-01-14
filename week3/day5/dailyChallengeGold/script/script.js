/*------------Daily Challenge GOLD: Bubble Sort------------*/

const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

/*q1 Using the .toString() method convert the array to a string.*/

let numbersString = numbers.toString();

/*q2 Using the .join()method convert the array to a string. Try passing different values into the join.*/

let numbersJoin = numbers.join(",")

/*q3 Bonus : To do this Bonus look up how to work with nested for loops
Sort the numbers array in descending order*/

for (let i = 0; i < numbers.length; i++) {
    for (let j = i; j < numbers.length; j++) {
        if (numbers[i] < numbers[j]) {
            let descendingSort = numbers[i];
            numbers[i] = numbers[j]
            numbers[j] = descendingSort;
        }
    }
}
console.log(numbers)