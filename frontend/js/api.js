const API_BASE_URL = "http://127.0.0.1:8000/api";

async function apiRequest(endpoint, options = {}) {
    const {
        method = "GET",
        body = null,
        headers = {}
    } = options;

    const requestHeaders = {
        ...headers,
        ...getAuthHeaders()
    };

    if (body !== null) {
        requestHeaders["Content-Type"] = "application/json";
    }

    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        method,
        headers: requestHeaders,
        body: body !== null ? JSON.stringify(body) : undefined
    });

    let responseData = null;

    const contentType = response.headers.get("content-type");

    if (contentType && contentType.includes("application/json")) {
        responseData = await response.json();
    } else {
        const text = await response.text();
        responseData = text || null;
    }

    if (!response.ok) {
        let message = "Something went wrong.";

        if (responseData) {
            if (typeof responseData === "string") {
                message = responseData;
            } else if (responseData.detail) {
                message = responseData.detail;
            }
        }

        if (response.status === 401) {
            clearToken();
        }

        throw new Error(message);
    }

    return responseData;
}
