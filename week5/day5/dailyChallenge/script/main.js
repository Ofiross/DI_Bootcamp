let num = '*'
function generate_table() {

    var body = document.getElementsByTagName("body")[0];

    var tbl = document.createElement("table");
    tbl.setAttribute('id', 'table')

    for (var i = 0; i < 7; i++) {
        var row = document.createElement("tr");

        for (var j = 0; j < 7; j++) {

            var cell = document.createElement("td");
            var cellText = document.createTextNode(num);
            cell.appendChild(cellText);
            row.appendChild(cell);
        }
        tbl.appendChild(row);
    }
    body.appendChild(tbl);
}
generate_table()

let tbl = document.getElementById('table')
