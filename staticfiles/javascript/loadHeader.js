document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("header-container");
    if (!container) {
      console.warn("No #header-container found. Header not loaded.");
      return;
    }
  
    fetch("/static/includes/header.html")
      .then(response => {
        if (!response.ok) {
          throw new Error("Failed to load header: " + response.status);
        }
        return response.text();
      })
      .then(html => {
        container.innerHTML = html;
      })
      .catch(err => {
        console.error("Header load error:", err);
      });
  });
  