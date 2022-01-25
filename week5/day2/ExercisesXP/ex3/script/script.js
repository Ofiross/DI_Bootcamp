/*----Exercise 3 : Transform The Sentence
----*/

//1. Create a global variable named allBoldItems.
let allBoldItems = "";



//2. Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

let getBold_items = () => {
    bold_Items = document.getElementsByTagName('strong');
};
getBold_items();

//3. Create a function called highlight() that changes the color of all the bold text to blue.
let highlight = () => {
    for (let i = 0; i < bold_Items.length; i++) {
        bold_Items[i].style.color = "blue"
    };
};


let return_normal = () => {
    for (let i = 0; i < bold_Items.length; i++) {
        bold_Items[i].style.color = "black"
    };
};

let p = document.getElementsByTagName('p')[0];
p.addEventListener("mouseover", highlight);
p.addEventListener("mouseout", return_normal)
