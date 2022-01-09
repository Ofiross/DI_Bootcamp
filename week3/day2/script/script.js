/*---------------Exercise 1: Your Favorite Food-----------------*/

let favoriteFood = "cheesecake"
let favoriteMeal = "dinner"

console.log(`I eat ${favoriteFood} at every ${favoriteMeal}`)



/*--------------------Exercise 2 : Series----------------*/
/*--------Part I--------*/
let watchedSeries = ["black mirror", "money heist", "the big bang theory"]

let watchedSeriesLength = watchedSeries.length;

let myWatchedSeries = "money heist"

console.log(`I watched 1 series: ${myWatchedSeries}`)

/*--------Part II--------*/
watchedSeries[2] = "friends"

watchedSeries.pop("greys anatomy")

watchedSeries.shift()

console.log("money heist".charAt(2))

console.log(watchedSeries)


/*---------Exercise 3 : The Temperature Converter-------*/

let celsius = 35

let fahrenheit = (35 / 5) * 9 + 32

console.log(`the celsius temperature ${celsius} is ${fahrenheit} in fahrenheit units`)


/*--------Exercise 4 : Guess The Answers #1--------*/


let c;
let a = 34;
let b = 21;

 /*q1*/   console.log(a + b) //first expression 
// Prediction: 55
// Actual: 55

a = 2;

 /*q2*/   console.log(a + b) //second expression
// Prediction: 23
// Actual: 23

/*q3*/    /*    c is equal undefined      */

/*q4*/    /* 75 as the computer assume that we had a mistake */


/*-----Exercise 5 : Guess The Answers #2------- */

typeof (15)
// Prediction: number
// Actual: number

typeof (5.5)
// Prediction: number
// Actual: number

typeof (NaN)
// Prediction: number
// Actual: number

typeof ("hello")
// Prediction: string
// Actual: string

typeof (true)
// Prediction: boolean
// Actual: boolean

typeof (1 != 2)
// Prediction: boolean
// Actual: boolean

"hamburger" + "s"
// Prediction: "hamburgers"
// Actual: "hamburgers"

"hamburgers" - "s"
// Prediction: NaN
// Actual: NaN

"1" + "3"
// Prediction: '13'
// Actual: '13'

"1" - "3"
// Prediction: '-2'
// Actual: '-2'

"johnny" + 5
// Prediction: 'johnny5'
// Actual: 'johnny5'

"johnny" - 5
// Prediction: NaN
// Actual: NaN

99 * "hello"
// Prediction: NaN
// Actual: NaN

1 != 1
// Prediction: false
// Actual: false

1 == "1"
// Prediction: true
// Actual: true

1 === "1"
// Prediction: false
// Actual: false


/*----Exercise 6 : Guess The Answers #3
Instructions----*/

5 + "34"
// Prediction: '534'
// Actual: '534'

5 - "4"
// Prediction: 1
// Actual: 1

10 % 5
// Prediction: 0
// Actual: 0

5 % 10
// Prediction: 5
// Actual: 5

"Java" + "Script"
// Prediction: 'JavaScript'
// Actual: 'JavaScript'


" " + " "
// Prediction: '  '
// Actual: '  '

" " + 0
// Prediction: ' 0'
// Actual: ' 0'

true + true
// Prediction: 2
// Actual: 2

true + false
// Prediction: 1
// Actual: 1

false + true
// Prediction: 1
// Actual: 1

false - true
// Prediction: -1  
// Actual: -1

!true
// Prediction: false
// Actual: false

3 - 4
// Prediction: -1   
// Actual: -1

"Bob" - "bill"
// Prediction: NaN
// Actual: NaN
