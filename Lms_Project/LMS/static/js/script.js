let accessToken = localStorage.getItem("accessToken") || ""
let currentUser = JSON.parse(localStorage.getItem("currentUser")) || null

function showModal(modalId) {
    document.getElementById(modalId).style.display = "block"
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = "none"
}

function toggleMenu() {
    document.getElementById("menu").classList.toggle("show")
}

function updateNavigation() {
    const loginLink = document.getElementById("loginLink")
    const registerLink = document.getElementById("registerLink")
    const logoutLink = document.getElementById("logoutLink")
    const fetchUsersLink = document.getElementById("fetchUsersLink")

    if (accessToken) {
        loginLink.style.display = "none"
        registerLink.style.display = "none"
        logoutLink.style.display = "inline-block"
        fetchUsersLink.style.display = "inline-block"
    } else {
        loginLink.style.display = "inline-block"
        registerLink.style.display = "inline-block"
        logoutLink.style.display = "none"
        fetchUsersLink.style.display = "none"
    }
}

async function registerUser() {
    const username = document.getElementById("reg_username").value
    const email = document.getElementById("reg_email").value
    const password = document.getElementById("reg_password").value
    const role = document.getElementById("reg_role").value

    try {
        const response = await fetch("http://127.0.0.1:8000/api/register/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username,
                email,
                password,
                role,
            }),
        })

        const data = await response.json()
        showNotification(
            response.ok ? "User Registered Successfully!" : data.detail || "Registration Error",
            response.ok ? "success" : "error",
        )

        if (response.ok) {
            setTimeout(() => closeModal("registerModal"), 2000)
        }
    } catch (error) {
        console.error("Registration error:", error)
        showNotification("An unexpected error occurred", "error")
    }
}

async function loginUser() {
    const username = document.getElementById("login_username").value
    const password = document.getElementById("login_password").value

    try {
        const response = await fetch("http://127.0.0.1:8000/api/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username,
                password,
            }),
        })

        const data = await response.json()

        if (response.ok) {
            accessToken = data.access
            currentUser = { username, role: data.role }
            localStorage.setItem("accessToken", accessToken)
            localStorage.setItem("currentUser", JSON.stringify(currentUser))
            showNotification("Login Successful!", "success")
            setTimeout(() => closeModal("loginModal"), 1000)
            updateNavigation()
            redirectBasedOnRole(data.role)
        } else {
            showNotification("Login Failed!", "error")
        }
    } catch (error) {
        console.error("Login error:", error)
        showNotification("An unexpected error occurred", "error")
    }
}

function redirectBasedOnRole(role) {
    console.log("Redirecting based on role:", role)
    if (role === "teacher") {
        window.location.href = "/assignments"
    } else if (role === "admin") {
        document.getElementById("adminControls").style.display = "block"
    } else {
        // For students, parents, or other roles
        showNotification("Welcome! You don't have access to the assignments page.", "info")
    }
}

function logoutUser() {
    accessToken = ""
    currentUser = null
    localStorage.removeItem("accessToken")
    localStorage.removeItem("currentUser")
    updateNavigation()
    document.getElementById("adminControls").style.display = "none"
    document.getElementById("userSection").style.display = "none"
    showNotification("Logged out successfully", "success")
}

async function fetchUsersByRole(role) {
    if (!accessToken) {
        showNotification("Please log in first!", "error")
        return
    }

    try {
        const response = await fetch(`http://127.0.0.1:8000/api/getdata/?role=${role}`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${accessToken}`,
            },
        })

        if (!response.ok) {
            throw new Error("Access Denied")
        }

        const users = await response.json()
        const usersHtml = users
            .map(
                (user) => `
            <li>
                <span><i class="fas fa-user"></i> ${user.username}</span>
                <span class="user-role">${user.role}</span>
                ${currentUser.role === "admin"
                        ? `
                    <button onclick="editUser('${user.id}')">Edit</button>
                    <button onclick="deleteUser('${user.id}')">Delete</button>
                `
                        : ""
                    }
            </li>
        `,
            )
            .join("")
        document.getElementById("usersList").innerHTML = usersHtml
        document.getElementById("userSection").style.display = "block"
    } catch (error) {
        console.error("Fetch users error:", error)
        document.getElementById("usersList").innerHTML = `<li class="error">${error.message}</li>`
        document.getElementById("userSection").style.display = "block"
    }
}

async function editUser(userId) {
    // Implement edit user functionality
    console.log("Edit user:", userId)
    // You can show a modal with a form to edit user details
}

async function deleteUser(userId) {
    if (confirm("Are you sure you want to delete this user?")) {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/users/${userId}`, {
                method: "DELETE",
                headers: {
                    Authorization: `Bearer ${accessToken}`,
                },
            })

            if (response.ok) {
                showNotification("User deleted successfully", "success")
                // Refresh the user list
                fetchUsersByRole(currentUser.role)
            } else {
                showNotification("Failed to delete user", "error")
            }
        } catch (error) {
            console.error("Delete user error:", error)
            showNotification("An unexpected error occurred", "error")
        }
    }
}

function showNotification(message, type) {
    const notification = document.getElementById("notification")
    notification.textContent = message
    notification.className = `notification ${type}`
    notification.classList.add("show")
    setTimeout(() => {
        notification.classList.remove("show")
    }, 3000)
}

// Close modal when clicking outside of it
window.onclick = (event) => {
    if (event.target.className === "modal") {
        event.target.style.display = "none"
    }
}

// Sticky Header
window.addEventListener("scroll", () => {
    var header = document.querySelector("header")
    header.classList.toggle("header-sticky", window.scrollY > 0)
})

// Initialize the page
document.addEventListener("DOMContentLoaded", () => {
    updateNavigation()
    if (currentUser) {
        redirectBasedOnRole(currentUser.role)
    }
})

// Attach event listeners
document.getElementById("fetchUsersLink").addEventListener("click", () => {
    if (accessToken) {
        fetchUsersByRole(currentUser.role)
    } else {
        showNotification("Please log in first!", "error")
    }
})

document.getElementById("logoutLink").addEventListener("click", logoutUser)

function addUser() {
    const username = document.getElementById("add_username").value
    const email = document.getElementById("add_email").value
    const password = document.getElementById("add_password").value
    const role = document.getElementById("add_role").value

    // Implement the API call to add a new user
    // This is a placeholder implementation
    console.log("Adding new user:", { username, email, role })
    showNotification("User added successfully", "success")
    closeModal("addUserModal")
}
