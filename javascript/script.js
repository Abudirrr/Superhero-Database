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

function updateMissionList() {
  const tableBody = document.getElementById("missionTable");
  tableBody.innerHTML = "";

  const keyword = document.getElementById("filterKeyword").value.toLowerCase();
  const priorityFilter = document.getElementById("filterPriority").value;
  const sortBy = document.getElementById("sortBy").value;

  let filteredMissions = missions.filter((m) => {
    const matchesKeyword = m.name.toLowerCase().includes(keyword);
    const matchesPriority = priorityFilter ? m.priority === priorityFilter : true;
    return matchesKeyword && matchesPriority;
  });

  if (sortBy === "name") {
    filteredMissions.sort((a, b) => a.name.localeCompare(b.name));
  } else if (sortBy === "date") {
    filteredMissions.sort((a, b) => new Date(a.dueDate) - new Date(b.dueDate));
  } else if (sortBy === "priority") {
    const priorityOrder = { High: 1, Medium: 2, Low: 3 };
    filteredMissions.sort((a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]);
  }

  filteredMissions.forEach((mission, index) => {
    const row = `
      <tr>
        <td>${mission.name}</td>
        <td>${mission.description}</td>
        <td>${mission.dueDate}</td>
        <td>${mission.priority}</td>
        <td>${mission.status}</td>
        <td>
          <button class="btn btn-success btn-sm" onclick="markCompleted(${index})">✔</button>
          <button class="btn btn-danger btn-sm" onclick="deleteMission(${index})">🗑</button>
        </td>
      </tr>
    `;
    tableBody.innerHTML += row;
  });

  document.getElementById("totalMissions").textContent = missions.length;
  document.getElementById("pendingMissions").textContent = missions.filter(m => m.status === "Pending").length;
  document.getElementById("completedMissions").textContent = missions.filter(m => m.status === "Completed").length;
}


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
