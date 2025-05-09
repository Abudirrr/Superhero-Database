// ✅ Superhero Mission Tracker - Enhanced

globalThis.missions = [];
let editIndex = -1;

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("missionForm");
  const toggle = document.getElementById("darkModeToggle");
  const body = document.body;

  // ✅ DARK MODE INIT
  if (localStorage.getItem("darkMode") === "enabled") {
    body.classList.add("dark-mode");
    if (toggle) toggle.checked = true;
  }

  if (toggle) {
    toggle.addEventListener("change", function () {
      body.classList.toggle("dark-mode", this.checked);
      localStorage.setItem("darkMode", this.checked ? "enabled" : "disabled");
    });
  }

  // ✅ FORM HANDLER
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();

      const name = document.getElementById("missionName").value.trim();
      const description = document.getElementById("missionDescription").value.trim();
      const dueDate = document.getElementById("missionDate").value;
      const priority = document.getElementById("missionPriority").value;

      if (!name || !description || !dueDate || !priority) {
        alert("Please fill in all fields.");
        return;
      }

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

      form.reset();
      updateMissionList();
    });
  }

  // ✅ LIVE FILTERS
  ["filterKeyword", "filterPriority", "sortBy"].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener("input", updateMissionList);
  });

  updateMissionList();
});

// ✅ UPDATE TABLE
function updateMissionList() {
  const tableBody = document.getElementById("missionTable");
  tableBody.innerHTML = "";

  const keyword = document.getElementById("filterKeyword")?.value.toLowerCase() || "";
  const priorityFilter = document.getElementById("filterPriority")?.value;
  const sortBy = document.getElementById("sortBy")?.value;

  let filtered = missions.filter(m => {
    return m.name.toLowerCase().includes(keyword) &&
      (!priorityFilter || m.priority === priorityFilter);
  });

  // ✅ SORT
  if (sortBy === "name") {
    filtered.sort((a, b) => a.name.localeCompare(b.name));
  } else if (sortBy === "date") {
    filtered.sort((a, b) => new Date(a.dueDate) - new Date(b.dueDate));
  } else if (sortBy === "priority") {
    const order = { High: 1, Medium: 2, Low: 3 };
    filtered.sort((a, b) => order[a.priority] - order[b.priority]);
  }

  filtered.forEach((mission, index) => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${mission.name}</td>
      <td>${mission.description}</td>
      <td>${mission.dueDate}</td>
      <td>${mission.priority}</td>
      <td>${mission.status}</td>
      <td>
        <button class="btn btn-success btn-sm" onclick="markCompleted(${index})">✔</button>
        <button class="btn btn-danger btn-sm" onclick="deleteMission(${index})">🗑</button>
      </td>
    `;

    tableBody.appendChild(row);
  });

  document.getElementById("totalMissions").textContent = missions.length;
  document.getElementById("pendingMissions").textContent = missions.filter(m => m.status === "Pending").length;
  document.getElementById("completedMissions").textContent = missions.filter(m => m.status === "Completed").length;
}

// ✅ COMPLETE MISSION
function markCompleted(index) {
  missions[index].status = "Completed";
  updateMissionList();
}

// ✅ DELETE MISSION
function deleteMission(index) {
  if (confirm("Are you sure you want to delete this mission?")) {
    missions.splice(index, 1);
    editIndex = -1;
    updateMissionList();
  }
}
