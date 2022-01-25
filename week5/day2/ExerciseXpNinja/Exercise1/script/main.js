/*-------Exercises XP Ninja -------*/
//Exercise 1 : Calculate The Tip
function calculateTip() {
    let billAmount = document.getElementById('billamt').value;
    let serviceQuality = document.getElementById('serviceQual').value;
    let numberOfPeople = document.getElementById('peopleamt').value;

    if (serviceQuality == 0 || billAmount === "") {
        alert('Please enter values');
    } else if (numberOfPeople === "" || numberOfPeople < 1) {
        numberOfPeople = 1
    }
    let total = ((billAmount * serviceQuality) / numberOfPeople).toFixed();
    let txt = document.createTextNode(`${total}`)
    document.getElementById('totalTip').style.display = "block"
    document.getElementById('tip').appendChild(txt)
}

let calculate = document.getElementById('calculate');
calculate.addEventListener('click', calculateTip);



