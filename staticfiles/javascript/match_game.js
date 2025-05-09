function checkMatch(inputId, correctName) {
    const inputElement = document.getElementById(inputId);
    if (!inputElement) {
        console.error("Input element not found for ID:", inputId);
        return;
    }

    const userInput = inputElement.value.trim().toLowerCase();
    const correct = correctName.toLowerCase();

    // Allow partial match (first letters) or full match
    if (userInput === correct || correct.startsWith(userInput)) {
        inputElement.classList.remove("is-invalid");
        inputElement.classList.add("is-valid");
        alert("✅ Correct! You matched " + correctName + ".");
    } else {
        inputElement.classList.remove("is-valid");
        inputElement.classList.add("is-invalid");
        alert("❌ Incorrect! Try again.");
    }
}
