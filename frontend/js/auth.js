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


function requireAuthentication() {
    if (!isAuthenticated()) {
        window.location.href = "login.html";
    }
}


function logout() {
    clearToken();
    window.location.href = "login.html";
}
