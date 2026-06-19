const API = "http://localhost:8000";

async function deleteVolunteer(id){

    const confirmDelete = confirm(
        "Are you sure you want to delete this volunteer?"
    );

    if(!confirmDelete) return;

    await fetch(
        `${API}/volunteers/${id}`,
        {
            method:"DELETE"
        }
    );

    loadDashboard();
}

async function loadDashboard(){

    const statsResponse =
    await fetch(`${API}/admin/stats`);

    const statsData =
    await statsResponse.json();

    document
    .getElementById("stats")
    .innerHTML =
    `
    <strong>Total Volunteers:</strong>
    ${statsData.total_volunteers}
    <br>
    <strong>Active Volunteers:</strong>
    ${statsData.active_volunteers}
    `;

    const volunteerResponse =
    await fetch(`${API}/volunteers`);

    const volunteers =
    await volunteerResponse.json();

    let html = `
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Skills</th>
        <th>Status</th>
        <th>Action</th>
    </tr>
    `;

    volunteers.forEach(v => {

        html += `
        <tr>
            <td>${v.id}</td>
            <td>${v.name}</td>
            <td>${v.email}</td>
            <td>${v.phone}</td>
            <td>${v.skills}</td>
            <td>${v.status}</td>
            <td>
                <button
                class="delete-btn"
                onclick="deleteVolunteer(${v.id})">
                Delete
                </button>
            </td>
        </tr>
        `;
    });

    document
    .getElementById("volunteerTable")
    .innerHTML = html;
}

loadDashboard();