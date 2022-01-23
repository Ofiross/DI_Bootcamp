/*Copy the code above and write some Javascript code to color all diagonal table cells in red.*/
let table = document.body.firstElementChild;

for (let i = 0; i < table.rows.length; i++) {
    let row = table.rows[i];
    row.cells[i].style.backgroundColor = 'red';
    for (let j = 0; j < table.rows.length; j++) {
        let row = table.rows[i];
        row.cells[i].style.backgroundColor = 'red';

    }
}