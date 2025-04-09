// ✅ Superhero Mission Tracker - script.js

// Array to hold missions
globalThis.missions = [];

// Currently editing index (-1 if not editing)
let editIndex = -1;

// ✅ Mission Form Handler
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("missionForm");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      const name = document.getElementById("missionName").value.trim();
      const description = document.getElementById("missionDescription").value.trim();
      const dueDate = document.getElementById("missionDate").value;
      const priority = document.getElementById("missionPriority").value;

      if (!name || !description || !dueDate || !priority) return;

      const newMission = {
        name,
        description,
        dueDate,
        priority,
        status: "Pending",
      };

      if (editIndex >= 0) {
        missions[editIndex] = { ...newMission, status: missions[editIndex].status };
        editIndex = -1;
      } else {
        missions.push(newMission);
      }

      updateMissionList();
      form.reset();
    });
  }
});

// ✅ Update Mission Table
function updateMissionList() {
  const tableBody = document.getElementById("missionTable");
  tableBody.innerHTML = "";

  missions.forEach((mission, index) => {
    const row = `
      <tr>
        <td>${mission.name}</td>
        <td>${mission.description}</td>
        <td>${mission.dueDate}</td>
        <td>${mission.priority}</td>
        <td>${mission.status}</td>
        <td>
          <button class="btn btn-success btn-sm" onclick="markCompleted(${index})">✔</button>
          <button class="btn btn-warning btn-sm" onclick="editMission(${index})">✎</button>
          <button class="btn btn-danger btn-sm" onclick="deleteMission(${index})">🗑</button>
        </td>
      </tr>`;
    tableBody.innerHTML += row;
  });

  document.getElementById("totalMissions").textContent = missions.length;
  document.getElementById("pendingMissions").textContent = missions.filter(m => m.status === "Pending").length;
  document.getElementById("completedMissions").textContent = missions.filter(m => m.status === "Completed").length;
}

// ✅ Mark Mission as Completed
function markCompleted(index) {
  if (missions[index]) {
    missions[index].status = "Completed";
    updateMissionList();
  }
}

// ✅ Delete Mission
function deleteMission(index) {
  missions.splice(index, 1);
  updateMissionList();
}

// ✅ Edit Mission
function editMission(index) {
  const mission = missions[index];
  document.getElementById("missionName").value = mission.name;
  document.getElementById("missionDescription").value = mission.description;
  document.getElementById("missionDate").value = mission.dueDate;
  document.getElementById("missionPriority").value = mission.priority;
  editIndex = index;

  document.querySelector("#missionForm button[type='submit']").textContent = "Update Mission";
}

// ✅ Contact Form (Optional)
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const name = document.getElementById("name").value;
      const email = document.getElementById("email").value;
      const subject = document.getElementById("subject").value;
      const message = document.getElementById("message").value;

      alert(`Message Sent!\n\nName: ${name}\nEmail: ${email}\nSubject: ${subject}\nMessage: ${message}`);
    });
  }
});

// ✅ Dark Mode Toggle
document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("darkModeToggle");
  const body = document.body;

  if (localStorage.getItem("darkMode") === "enabled") {
    body.classList.add("dark-mode");
    if (toggle) toggle.checked = true;
  }

  if (toggle) {
    toggle.addEventListener("change", function () {
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
