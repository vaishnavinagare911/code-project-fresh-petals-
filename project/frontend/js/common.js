var BASE_URL = "http://127.0.0.1:5000/api";

function getToken() {
  return localStorage.getItem("token");
}

function getRole() {
  return localStorage.getItem("userRole") || "";
}

function setUserRole(role) {
  if (role) localStorage.setItem("userRole", role);
  else localStorage.removeItem("userRole");
}

function isLoggedIn() {
  return !!getToken();
}

function isAdmin() {
  return getRole() === "admin";
}

function logout() {
  localStorage.removeItem("token");
  localStorage.removeItem("userRole");
  localStorage.removeItem("userName");
  localStorage.removeItem("userEmail");
  window.location.href = "login.html";
}

function authHeaders() {
  const token = getToken();
  return {
    "Content-Type": "application/json",
    ...(token ? { Authorization: "Bearer " + token } : {}),
  };
}

function renderHeader(currentPage) {
  const header = document.querySelector("header");
  if (!header) return;

  const token = getToken();
  const siteName = "Freshpetals";

  const role = token ? getRole() : "";
  const navLinks = token
    ? [
        { href: "index.html", label: "Home" },
        { href: "about.html", label: "About" },
        { href: "wishlist.html", label: "Wishlist" },
        { href: "cart.html", label: "Cart" },
        { href: "orders.html", label: "My Orders" },
        ...(role === "admin" ? [{ href: "admin.html", label: "Admin" }] : []),
        { href: "profile.html", label: "Profile" },
        { href: "#", label: "Logout", onclick: "logout()" },
      ]
    : [
        { href: "index.html", label: "Home" },
        { href: "about.html", label: "About" },
        { href: "login.html", label: "Login" },
        { href: "register.html", label: "Register" },
      ];

  const navHtml = navLinks
    .map((link) => {
      if (link.onclick) {
        return `<a href="#" onclick="logout(); return false;" class="nav-link">Logout</a>`;
      }
      const active = currentPage === link.label ? ' class="active"' : "";
      return `<a href="${link.href}" class="nav-link"${active}>${link.label}</a>`;
    })
    .join("");

  header.innerHTML = `
    <a href="index.html" class="logo">${siteName}</a>
    <nav class="nav-links">${navHtml}</nav>
    <button class="mobile-menu-btn" aria-label="Menu" onclick="toggleMobileMenu()">
      <span></span><span></span><span></span>
    </button>
  `;
}

function toggleMobileMenu() {
  document.body.classList.toggle("mobile-menu-open");
}


document.addEventListener("click", (e) => {
  if (e.target.closest(".nav-links a")) {
    document.body.classList.remove("mobile-menu-open");
  }
});