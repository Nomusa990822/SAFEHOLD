const TOKEN_KEY = "safehold_access_token";

function saveToken(token) {
    localStorage.setItem(TOKEN_KEY, token);
}

function getToken() {
    return localStorage.getItem(TOKEN_KEY);
}

function clearToken() {
    localStorage.removeItem(TOKEN_KEY);
}

function isAuthenticated() {
    return Boolean(getToken());
}

function getAuthHeaders() {
    const token = getToken();

    if (!token) {
        return {};
    }

    return {
        Authorization: `Bearer ${token}`
    };
}

async function registerUser(userData) {
    return apiRequest("/auth/register", {
        method: "POST",
        body: userData
    });
}

async function loginUser(email, password) {
    const response = await apiRequest("/auth/login", {
        method: "POST",
        body: {
            email,
            password
        }
    });

    if (!response.access_token) {
        throw new Error("Login failed. No access token was returned.");
    }

    saveToken(response.access_token);

    return response;
}

async function getCurrentUser() {
    return apiRequest("/auth/me", {
        method: "GET"
    });
}

function requireAuthentication() {
    if (!isAuthenticated()) {
        window.location.href = "login.html";
    }
}

function redirectIfAuthenticated() {
    if (isAuthenticated()) {
        window.location.href = "pages/home.html";
    }
}

function logout() {
    clearToken();
    window.location.href = "../index.html";
}
