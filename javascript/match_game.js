function checkMatch(inputId, correctName) {
    let userInput = document.getElementById(inputId).value.trim().toLowerCase();
    let correctNameLower = correctName.toLowerCase();
    
    // Allow partial name matches
    if (userInput && correctNameLower.startsWith(userInput)) {
        alert("Correct! You matched " + correctName);
    } else {
        alert("Incorrect! Try again.");
    }
}
