let createCalendar = (year, month) => {
    //creating a table header with days
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

    //searching for the first day of the month 0 for sunday untill 6 for saturday
    const firstDay = (new Date(`${month}, 1, ${year}`)).getDay();
    console.log(firstDay)

    //starting day of the month
    let date = 1;
    //creating rows for calander
    for (let i = 0; i < 6; i++) {

        let row = document.createElement("tr");

        //creating days for month calander table
        //base on the index of the starting day of the month, the days will stard as empty string with out number inside
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                cell = document.createElement("td");
                cellText = document.createTextNode("");
                cell.appendChild(cellText);
                row.appendChild(cell);
            }
            //if the date is bigger than the days in the month break out from the loop to stop creating days
            else if (date > daysInMonth(month, year)) {
                break;
            }
            //creates the dates starting from 1 to the days in the month.
            else {
                cell = document.createElement("td");
                cellText = document.createTextNode(date);
                cell.appendChild(cellText);
                row.appendChild(cell);
                date++;
            }
            //adding all to our table
            tblBody.appendChild(row);
        }
        tbl.appendChild(tblBody);
        body.appendChild(tbl);
        tbl.setAttribute("border", "2");

    }


}

//function to check how many days are in a year
let daysInMonth = (month, year) => {

    return new Date(year, month, 0).getDate();
};