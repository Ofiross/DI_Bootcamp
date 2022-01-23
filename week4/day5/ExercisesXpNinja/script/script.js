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

    const firstDay = new Date(year, month, 0).getDay();
    console.log(firstDay)

    const date = firstDay + 1;

    for (var i = 0; i < 5; i++) {

        var row = document.createElement("tr");

        for (var j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                let cell = document.createElement("td");
                let cellText = document.createTextNode('');
                cell.appendChild(cellText);
                row.appendChild(cell);
            } else if (date > daysInMonth(month, year)) {
                break;
            } else {
                cell = document.createElement("td");
                let cellText = document.createTextNode(firstDay)
                cell.setAttribute("data-date", date);
                cell.setAttribute("data-month", month + 1);
                cell.setAttribute("data-year", year);
                cell.className = "date-picker";
                cell.innerHTML = "<span>" + date + "</span>";
                row.appendChild(cell);


            }

            tblBody.appendChild(row);
        }

        tbl.appendChild(tblBody);
        body.appendChild(tbl);
        tbl.setAttribute("border", "2");
    }
}
let daysInMonth = (month, year) => {

    return new Date(year, month, 0).getDate();
};
