/*---Daily Challenge: Tell The Story---*/

//1. Get the value of each of the inputs in the HTML file when the button is clicked.
const button = document.getElementById('lib-button');
let inp = document.querySelectorAll('input')
let storyAsString = ""
let arrFromStr = []
let makeAstory = () => {

    let storyResult = document.getElementById("story")
    let noun = document.getElementById("noun").value;
    let adj = document.getElementById("adjective").value;
    let name = document.getElementById("person").value;
    let verb = document.getElementById("verb").value;
    let place = document.getElementById("place").value;

    //2. Make sure the values are not empty
    for (let i = 0; i < inp.length; i++) {
        if (inp[i].value.length == 0) {
            alert("You forgot to fill one of the fileds");
            return false;
        };
    };

    //3. Write a story that uses each of the values.
    storyResult.innerHTML = noun + " " + adj + " " + name + " " + verb + " " + place;
    storyAsString = (noun + " " + adj + " " + name + verb + " " + place);
    arrFromStr = storyAsString.split(" ",)

};

button.addEventListener('click', makeAstory);


//5. Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.
let shuffleArray = (arr) => {
    let currentIndex = arr.length, temporaryValue, randomIndex;
    while (0 !== currentIndex) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = arr[currentIndex];
        arr[currentIndex] = arr[randomIndex];
        arr[randomIndex] = temporaryValue;
    }
    return arr;
}

let shuffleMe = () => {
    let shuffledStory = document.getElementById("shuffledStory");

    shuffledStory.innerHTML = shuffleArray(arrFromStr);
};

let SflBtn = document.getElementById('shuffle');
SflBtn.addEventListener('click', shuffleMe)




