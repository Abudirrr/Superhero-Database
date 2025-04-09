document.addEventListener("DOMContentLoaded", function () {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const body = document.body;
  
    // ✅ Apply saved theme
    if (localStorage.getItem("darkMode") === "enabled") {
      body.classList.add("dark-mode");
      if (darkModeToggle) darkModeToggle.checked = true;
    }
  
    // ✅ Listen for toggle changes
    if (darkModeToggle) {
      darkModeToggle.addEventListener("change", function () {
        if (this.checked) {
          body.classList.add("dark-mode");
          localStorage.setItem("darkMode", "enabled");
        } else {
          body.classList.remove("dark-mode");
          localStorage.setItem("darkMode", "disabled");
        }
      });
    }
  });
  