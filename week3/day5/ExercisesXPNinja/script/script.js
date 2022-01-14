/*-------------Exercise 1 : Checking The BMI-------------*/

/*q1 Create two objects, each object should hold a person’s details. Here are the details: FullName Mass Height*/
let person1 = {
    FullName: "John",
    Mass: 85,
    Height: 1.85,
    BMI: function () {
        console.log(this.Mass / (this.Height ** 2))
    }
}

let person2 = {
    FullName: "Tom",
    Mass: 90,
    Height: 1.88,
    BMI: function () {
        console.log(this.Mass / (this.Height ** 2))
    }
}

/*q3 Outside of the objects, create a JS function that compares the BMI of both objects.*/
/*q4 Display the name of the person who has the largest BMI.*/

function whoIsBigger() {
    let x = person1.Mass / (person2.Height ** 2)
    let y = person2.Mass / (person2.Height ** 2)
    if (x > y) {
        console.log(person1.FullName)
    } else {
        console.log(person2.FullName)
    }
}
whoIsBigger();


/*---------------------Exercise 2 : Grade Average---------------*/
let gradesList = [65, 55, 40, 60, 45]

let findAvg = (gradesList) => {
    let sum = 0;

    for (i = 0; i < gradesList.length; i++) {
        sum += gradesList[i];
    }
    return sum / gradesList.length;
};
findAvg(gradesList)

let passOrNo = () => {
    if (findAvg(gradesList) > 65) {
        return "pass"
    } else {
        return "failed and must repeat the course!!!"
    }
};
passOrNo()