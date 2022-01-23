/*------------Exercises XP Gold-----------*/

/*---Exercise 1 : My Book List---*/
/*1. In the body of the HTML page, create an empty div*/

/*2. n the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys
3. Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)*/



let allBooks = [
    {
        title: "The Mamba Mentality",
        author: "Nissim Mishal",
        image: "https://images-na.ssl-images-amazon.com/images/I/91OOQmM8YlL.jpg",
        alreadyRead: true
    },

    {
        title: "Mossad: The Greatest Missions of the Israeli Secret Service",
        author: "kobe bryant",
        image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw-fy9gR2uUwMC010Rzb7VQbouOfiyerQYaQ&usqp=CAU",
        alreadyRead: true
    }
];

/*4.Requirements : All the instructions below need to be coded in the js file:
Using the DOM, render the books inside an HTML table (the HTML table must be added to the <div> created in part 1).
For each book :
You have to display the book’s title and the book’s author.
Example: HarryPotter written by JKRolling.
The width of the image has to be set to 100px.
If the book is already read. Set the color of the book’s details to red.*/
let header = ['Title', 'Author', 'Image', 'Read'];

const booksTable = () => {
    let tbl = document.createElement("table")
    tbl.style.width = '100%';
    tbl.setAttribute('border', '2');
    let divByName = document.getElementsByClassName("listBooks")[0]
    divByName.appendChild(tbl)
    divByName.getElementsByTagName("table")[0].setAttribute("id", "books")


    let headerRow = document.createElement('tr');

    header.forEach(headertext => {
        let header = document.createElement('th');
        let textNode = document.createTextNode(headertext);
        header.appendChild(textNode);
        headerRow.appendChild(header);
    })

    tbl.appendChild(headerRow);

    allBooks.forEach(bk => {
        let row = document.createElement('tr');


        Object.values(bk).forEach(text => {
            let cell = document.createElement('td')
            let textNode = document.createTextNode(text);

            cell.appendChild(textNode);
            if (alreadyRead = true) {
                row.style.background = 'red'
            }
            row.appendChild(cell);

        })
        tbl.appendChild(row);
    })
}
booksTable(allBooks);









