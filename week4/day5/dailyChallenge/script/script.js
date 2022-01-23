/*1. Create an array which value is the planets of the solar system.
2. For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
3. Each planet should have a different background color. (Hint: add a new class to each planet).
4. Finally append each div to the <section> in the HTML (presented below).
5. Bonus: Do the same process to create the moons.
Be careful, each planet has a certain amount of moons. How should you display them?
Should you still use an array for the planets ? Or an array of objects ?*/

let planetsOfSlSs = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

planetsOfSlSs.forEach(e => {
    let planetsDiv = document.createElement('div');
    planetsDiv.setAttribute('class', e);
    planetsDiv.classList.add('planet')
    document.getElementsByClassName('listPlanets')[0].appendChild(planetsDiv)
});

document.getElementsByClassName('Mercury')[0].style.backgroundColor = "lightblue";
document.getElementsByClassName('Venus')[0].style.backgroundColor = "#EFE587"
document.getElementsByClassName('Earth')[0].style.backgroundColor = "#6781EB"
document.getElementsByClassName('Mars')[0].style.backgroundColor = "#F27171"
document.getElementsByClassName('Jupiter')[0].style.backgroundColor = "#B9D5D7"
document.getElementsByClassName('Saturn')[0].style.backgroundColor = "#DADBC5"
document.getElementsByClassName('Uranus')[0].style.backgroundColor = "#B0FBFF"
document.getElementsByClassName('Neptune')[0].style.backgroundColor = "#7C89CE"

let moons = { Mercury: 0, Venus: 0, Earth: 1, Mars: 2, Jupiter: 53, Saturn: 53, Uranus: 27, Neptune: 14 }


Object.keys(moons).forEach(num => {
    if (moons[num] > 0) {
        let moonsDiv = document.createElement('div');
        moonsDiv.setAttribute('class', num + "moon");
        moonsDiv.classList.add('moon')
        document.getElementsByClassName(num)[0].appendChild(moonsDiv)
        let text = document.createTextNode(moons[num]);
        document.getElementsByClassName(num + 'moon')[0].appendChild(text)
    }
});