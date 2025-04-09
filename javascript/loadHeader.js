document.addEventListener("DOMContentLoaded", function () {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "header.html", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("header-container").innerHTML = xhr.responseText;
        } else if (xhr.readyState === 4) {
            console.error("Error loading the header:", xhr.status);
        }
    };
    xhr.send();
});
