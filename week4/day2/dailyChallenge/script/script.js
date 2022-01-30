/*--------------Daily Challenge------------*/
let starsAround = () => {
    let str = prompt("Please insert a sentence with comma between each word").split(',')
        .map(item => '' + item
            .trim());

    let longestWord = 0;
    for (let i = 0; i < str.length; i++) {
        if (str[i].length > longestWord) {
            longestWord = str[i].length
        }
    }
    let stars = "*".repeat(longestWord + 4)
    str = str.map(wd => { return wd + (new Array(longestWord - wd.length).fill(' ').join('')) });


    let newStr = str.map(w => '* ' + w + ' *');
    newStr.push(stars)
    newStr.splice(0, 0, stars)


    console.log(newStr.join(`\n`))
}