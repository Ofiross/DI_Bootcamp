/***************Daily Challenge To Do List ***************/


let addTask = () => {
    let listTask = [];
    let tasksMainList = document.getElementById('tasks');
    let tasktext = document.getElementById('taskAdder');
    if (tasktext.value == "") {
        alert("Please add task");
        return false
    } else {
        listTask.push(tasktext);
    }
    listTask.forEach(txt => {
        let li = document.createElement('li');
        li.setAttribute('id', 'addedTask');
        li.style.listStyle = 'none';
        let btn = document.createElement('button');
        btn.setAttribute('class', 'delete');
        let icn = document.createElement('i');
        icn.setAttribute('class', 'fas fa-trash-alt');
        btn.appendChild(icn)
        btn.style.textAlign = 'center';
        btn.style.backgroundColor = '#FF2D2D';
        btn.style.color = 'white';
        btn.style.border = 'transparent';
        btn.style.borderRadius = '2px';
        li.appendChild(btn);
        let check = document.createElement('input');
        check.type = 'checkbox';
        check.setAttribute('id', 'check')
        let label = document.createElement('label');
        li.appendChild(check);
        let task = document.createTextNode(txt.value);
        label.appendChild(task);
        li.appendChild(label);
        tasksMainList.appendChild(li);
    })
    tasktext.value = "";

    let close = document.getElementsByClassName("delete");
    for (let i = 0; i < close.length; i++) {
        close[i].addEventListener('click', e => {
            var mom = close[i].parentElement;
            mom.style.display = "none";
        })
    };
};

let form = document.querySelector('form')
form.addEventListener("submit", e => {
    e.preventDefault();
    addTask();
});


var tasksListChecker = document.querySelector('ul');
tasksListChecker.addEventListener('click', ev => {
    if (ev.target.classList.toggle('checked')) {
        ev.target.nextSibling.style.textDecoration = "line-through"
    } else {
        console.log('bye')
        ev.target.nextSibling.style.textDecoration = "none"
    }
});


function reload() {
    reload = location.reload();
}

let clear = document.getElementById('clearButton')
clearButton.addEventListener('click', reload)
