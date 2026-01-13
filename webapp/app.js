const loginSection = document.getElementById("login-section"); // login section
const dashboardSection = document.getElementById("dashboard-section"); // dashboard section

const usernameEl = document.getElementById("username");
const passwordEl = document.getElementById("password");
const loginBtn = document.getElementById("login-btn");
const loginMsg = document.getElementById("login-msg");

const welcomeMsg = document.getElementById("welcome-msg");
const logoutBtn = document.getElementById("logout-btn");

const searchInput = document.getElementById("search-input");
const searchBtn = document.getElementById("search-btn");
const searchResults = document.getElementById("search-results");

const titleEl = document.getElementById("title");
const descEl = document.getElementById("desc");
const submitTicketBtn = document.getElementById("submit-ticket-btn");
const ticketMsg = document.getElementById("ticket-msg");

// Demo data
const VALID_USER = "admin";
const VALID_PASS = "1234";

const PRODUCTS = ["radar", "sensor", "camera", "drone", "shield", "firmware"];

function showDashboard(username) {
  loginSection.classList.add("hidden");
  dashboardSection.classList.remove("hidden");
  welcomeMsg.textContent = `Welcome, ${username}!`;
}

function showLogin() {
  dashboardSection.classList.add("hidden");
  loginSection.classList.remove("hidden");

  // reset
  usernameEl.value = "";
  passwordEl.value = "";
  loginMsg.textContent = "";
  ticketMsg.textContent = "";
  searchResults.innerHTML = "";
}

loginBtn.addEventListener("click", () => {
  const u = usernameEl.value.trim();
  const p = passwordEl.value.trim();

  if (u === VALID_USER && p === VALID_PASS) {
    loginMsg.textContent = "";
    showDashboard(u);
  } else {
    loginMsg.textContent = "Invalid credentials";
    loginMsg.style.color = "crimson";
  }
});

logoutBtn.addEventListener("click", () => {
  showLogin();
});

// Search
searchBtn.addEventListener("click", () => {
  const q = searchInput.value.trim().toLowerCase();
  searchResults.innerHTML = "";

  const matches = PRODUCTS.filter(x => x.includes(q) && q.length > 0);

  if (matches.length === 0) {
    const li = document.createElement("li");
    li.textContent = "No results";
    searchResults.appendChild(li);
    return;
  }

  matches.forEach(m => {
    const li = document.createElement("li");
    li.textContent = m;
    searchResults.appendChild(li);
  });
});

// Form
submitTicketBtn.addEventListener("click", () => {
  const title = titleEl.value.trim();
  const desc = descEl.value.trim();

  if (title.length < 3) {
    ticketMsg.textContent = "Title must be at least 3 chars";
    ticketMsg.style.color = "crimson";
    return;
  }
  if (desc.length < 5) {
    ticketMsg.textContent = "Description must be at least 5 chars";
    ticketMsg.style.color = "crimson";
    return;
  }

  ticketMsg.textContent = "Ticket submitted successfully!";
  ticketMsg.style.color = "green";
});
