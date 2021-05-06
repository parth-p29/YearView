function goals(){
    
    const add = document.querySelector('.add-button button');

    if (add.innerHTML === "Add Pictures") {

        document.getElementById('add-pics').style.display="flex";
        add.innerHTML = "Close";
    }

    else if (add.innerHTML === "Close") {

        document.getElementById('add-pics').style.display="none";
        add.innerHTML = "Add Pictures";

    }
}
