/*--------------Exercise 1 : The World Translator------------*/

/*q1 Ask the user which language they speak*/
let userLanguage = prompt(`What language do you speak?`)

/*q2 Convert the user’s answer to lowercase*/
let userLanguageLower = userLanguage.toLocaleLowerCase();

/*q3 
Create a few conditions :
If the user speaks French : display “Bonjour”
If the user speaks English : display “Hello”
If the user speaks Hebrew : display “Shalom”
If the user doesn’t speak any of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’*/

switch (userLanguageLower) {
    case 'french':
        greet = "Bonjour";
        alert(`${greet}`);
        break;
    case 'english':
        greet = "Hello";
        alert(`${greet}`);
        break
    case 'hebrew':
        greet = "Shalom";
        alert(`${greet}`);
        break
    default:
        greet = "01110011 01101111 01110010 01110010 01111001";
        alert(`${greet}`);
        break
};


/*--------------Exercise 2 : The Grade Assigner------------*/

/*q1 Ask the user for their grade*/
let userGrade = prompt(`What is your grade?`)

/*q2 If the grade is bigger than 90, console.log “A”*/

userGradeInput = [
    userGrade >= 90,
    userGrade <= 90 && userGrade >= 80,
    userGrade >= 70 && userGrade <= 80
]

switch (userGradeInput.indexOf(true)) {
    case 0:
        console.log("A");
        break;
    case 1:
        console.log("B");
        break;
    case 2:
        console.log("C");
        break;
    default:
        console.log("D");
        break;
};


/*--------------Exercise 3 : Verbing------------*/

/*q1 Prompt the user for a string. It must be a verb*/
let userVerb = prompt(`Please insert a verb, nothing else, only a verb!!!`);
let userVerbLower = userVerb.toLocaleLowerCase();

/*q2 If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string*/

/*q3 If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end*/

/*q4 If the length of the string is less than 3, leave it unchanged*/

userVerbOfChoice = [
    userVerbLower.length > 3 && userVerbLower.endsWith("ing") == false,
    userVerbLower.length > 3 && userVerbLower.endsWith("ing") == true
]

switch (userVerbOfChoice.indexOf(true)) {
    case 0:
        changeTo = userVerbLower + "ing";
        console.log(changeTo)
        break;
    case 1:
        changeTo = userVerbLower + "ly";
        console.log(changeTo)
        break;
    default:
        undefined
        console.log(userVerbLower)
        break;
};
