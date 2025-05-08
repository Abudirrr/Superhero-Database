document.addEventListener("DOMContentLoaded", function () {
  const body = document.body;

  // Apply saved dark mode preference
  if (localStorage.getItem("darkMode") === "enabled") {
    body.classList.add("dark-mode");
  }

  function setupToggle() {
    const darkModeToggle = document.getElementById("darkModeToggle");

    if (!darkModeToggle) return;

    // Set checkbox state based on preference
    darkModeToggle.checked = localStorage.getItem("darkMode") === "enabled";

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

  // Initial setup
  setupToggle();

  // OPTIONAL: Re-check if the header was loaded dynamically (e.g., with jQuery)
  const observer = new MutationObserver(() => {
    if (document.getElementById("darkModeToggle")) {
      setupToggle();
      observer.disconnect();
    }
  });

  observer.observe(document.body, { childList: true, subtree: true });
});
