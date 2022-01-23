let createCalendar = (year, month) => {

    const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];


    let body = document.getElementsByTagName('body')[0]

    let tbl = document.createElement("table");
    let tblBody = document.createElement("tbody");

    let headerRow = document.createElement('tr');

    days.forEach(headertext => {
        let days = document.createElement('th');
        let textNode = document.createTextNode(headertext);
        days.appendChild(textNode);
        headerRow.appendChild(days);
    })

    tblBody.appendChild(headerRow);

    const firstDay = new Date(year, month, 6).getDay();
    console.log(firstDay)
    today = new Date();

    let date = 1;
    for (let i = 0; i < 6; i++) {
        // creates a table row
        let row = document.createElement("tr");

        //creating individual cells, filing them up with data.
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                cell = document.createElement("td");
                cellText = document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }
            else if (date > daysInMonth(month, year)) {
                break;
            }

            else {
                cell = document.createElement("td");
                cellText = document.createTextNode(date);
                if (date === today.getDate() && year === today.getFullYear() && month === today.getMonth()) {
                    cell.classList.add("bg-info");
                } // color today's date
                cell.appendChild(cellText);
                row.appendChild(cell);
                date++;
            }

            tblBody.appendChild(row); // appending each row into calendar body
        }
        tbl.appendChild(tblBody);
        body.appendChild(tbl);
        tbl.setAttribute("border", "2");

    }


}


let daysInMonth = (month, year) => {

    return new Date(year, month, 0).getDate();
};