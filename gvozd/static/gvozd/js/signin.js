var button = document.getElementById("button");
var button2 = document.getElementById("button2");
var nameText = document.getElementById("name_text");
var emailText = document.getElementById("email_text");
var nameObj = document.getElementById("name");
var emailObj = document.getElementById("e-mail");
var passObj = document.getElementById("pass");
var passText = document.getElementById("pass_text");
var err1 = document.getElementById("err1");
var err1 = document.getElementById("err1");
var err1 = document.getElementById("err1");
var modal = document.getElementsByClassName("modal")[0];
var closeBtn = document.getElementsByClassName("close_btn")[0];
var mailformat = /[0-9a-z_-]+@[0-9a-z_-]+\.[a-z]{2,5}/i;

button.onclick = function () {
    var name = document.querySelector("#name").value;
    var email = document.querySelector("#e-mail").value;
    var service = document.querySelector("#pass");
    if (name < 1) {
        err1.style.display = "block";
        nameText.style.color = "red";
        return 0;
    }
    if (email < 1) {
        err2.style.display = "block";
        emailText.style.color = "red";
        return 0;
    }
    if (service.selectedIndex == 0) {
        err3.style.display = "block";
        passText.style.color = "red";
        return 0;
    }
    if (!email.match(mailformat)) {
        err2.style.display = "block";
        emailText.style.color = "red";
        return 0;
    }
    err1.style.display = "none";
    err2.style.display = "none";
    err3.style.display = "none";
    nameText.style.color = "white";
    emailText.style.color = "white";
    passText.style.color = "white";
    modal.style.display = "block";
    nameObj.disabled = "true";
    emailObj.disabled = "true";
    passObj.disabled = "true";
    button.style.display = "none"
    button2.style.display = "none"
    return 1;

}

button2.onclick = function () {
    nameObj.value = "";
    emailObj.value = "";
    passObj.value = "";
}

closeBtn.onclick = function () {
    modal.style.display = "none";
}