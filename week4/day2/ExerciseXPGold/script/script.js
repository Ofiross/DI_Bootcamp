/*-------------Exercise 1 : Is_Blank---------------*/
/*Write a program to check whether a string is blank or not.*/

let isBlank = (string) => {
    if (string === '') {
        return true
    } else {
        return false
    }
};


/*-------------Exercise 2 : Abbrev_name------------*/
let abbrevName = (abb) => {

    let splited = abb.split(" ",);
    let newAbb = splited[0] + " " + splited[1][0] + ".";
    console.log(newAbb);
}


/*----------------Exercise 3 : SwapCase------------*/
let swapsTheCase = (toChange) => {
    let splitStr = toChange.toLowerCase().split(' ');
    for (let i = 0; i < splitStr.length; i++) {
        splitStr[i] = splitStr[i].charAt(0).toLowerCase() + splitStr[i].substring(1).toUpperCase();
    }
    return splitStr.join(' ');
};


/*----------Exercise 4 : Omnipresent Value-----------*/
let isOmnipresent = (arr, val) => arr.every(x => x.includes(val));

