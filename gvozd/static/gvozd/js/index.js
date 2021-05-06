slide01 = document.getElementById("slide_01");
slide02 = document.getElementById("slide_02");
slide03 = document.getElementById("slide_03");
arrow01Left = document.getElementById("arrow_01_left");
arrow01Right = document.getElementById("arrow_01_right");
arrow02Left = document.getElementById("arrow_02_left");
arrow02Right = document.getElementById("arrow_02_right");
arrow03Left = document.getElementById("arrow_03_left");
arrow03Right = document.getElementById("arrow_03_right");
indicator = document.getElementById("indicator");

arrow01Left.onclick = function () {
    slide01.style.display = "none";
    slide03.style.display = "flex";
    indicator.src = "/жаба/3iz3.png";

}

arrow01Right.onclick = function () {
    slide01.style.display = "none";
    slide02.style.display = "flex";
    indicator.src = "/жаба/2iz3.png";
}

arrow02Left.onclick = function () {
    slide02.style.display = "none";
    slide01.style.display = "flex";
    indicator.src = "/жаба/1iz3.png";
}

arrow02Right.onclick = function () {
    slide02.style.display = "none";
    slide03.style.display = "flex";
    indicator.src = "/жаба/3iz3.png";
}

arrow03Left.onclick = function () {
    slide03.style.display = "none";
    slide02.style.display = "flex";
    indicator.src = "/жаба/2iz3.png";
}

arrow03Right.onclick = function () {
    slide03.style.display = "none";
    slide01.style.display = "flex";
    indicator.src = "/жаба/1iz3.png";
}