const API_BASE_URL = "http://127.0.0.1:8000/api";


async function apiRequest(
    endpoint,
    options = {}
) {
    const token = getToken();

    const headers = {
        ...(options.headers || {})
    };

    if (!headers["Content-Type"] && !(options.body instanceof FormData)) {
        headers["Content-Type"] = "application/json";
    }

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            ...options,
            headers
        }
    );

    const contentType =
        response.headers.get("content-type") || "";

    let data = null;

    if (response.status !== 204) {
        data = contentType.includes("application/json")
            ? await response.json()
            : await response.text();
    }

    if (!response.ok) {
        throw new Error(
            data?.detail ||
            "Something went wrong."
        );
    }

    return data;
}
