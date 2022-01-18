/*--------------Daily Challenge------------*/
let starsAround = () => {
    let str = prompt("Please insert a sentence with comma between each word")
    let wordLength = str.split(',').map(item => '' + item.trim());
    let longestWord = 0;
    let string = ""
    for (let i = 0; i < wordLength.length; i++) {
        if (wordLength[i].length > longestWord) {
            longestWord = wordLength[i].length + 4
        }
        for (let j = 0; j < wordLength.length; j++) {
            if (wordLength[j].length < longestWord) {
                string += " "
            } else {
                string = ""
            }

        }
    }
    let arrayFromString = str.split(',').map(item => '* ' + item.trim() + (`${string} *`));
    let star = "*"
    let stars = star.repeat(longestWord)
    arrayFromString.push(stars)
    arrayFromString.splice(0, 0, stars)
    console.log(arrayFromString.join(`\n`))
}