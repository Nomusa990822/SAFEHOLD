async function createIncident(incidentData) {
    return await apiRequest(
        "/incidents",
        {
            method: "POST",
            body: JSON.stringify(incidentData)
        }
    );
}


async function getIncidents() {
    return await apiRequest(
        "/incidents"
    );
}


async function getIncident(incidentId) {
    return await apiRequest(
        `/incidents/${incidentId}`
    );
}


async function updateIncident(
    incidentId,
    incidentData
) {
    return await apiRequest(
        `/incidents/${incidentId}`,
        {
            method: "PATCH",
            body: JSON.stringify(incidentData)
        }
    );
}


async function deleteIncident(incidentId) {
    return await apiRequest(
        `/incidents/${incidentId}`,
        {
            method: "DELETE"
        }
    );
}
