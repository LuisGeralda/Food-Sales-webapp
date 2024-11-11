// File: script.js
// Location: frontend/

async function loadDropdownOptions() {
    const response = await fetch('http://127.0.0.1:5000/unique-values');
    const data = await response.json();

    const cityDropdown = document.getElementById('city');
    data.cities.forEach(city => {
        const option = document.createElement('option');
        option.value = city;
        option.text = city;
        cityDropdown.add(option);
    });

    const categoryDropdown = document.getElementById('category');
    data.categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.text = category;
        categoryDropdown.add(option);
    });
}

async function fetchData() {
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const city = document.getElementById('city').value;
    const category = document.getElementById('category').value;

    const response = await fetch(`http://127.0.0.1:5000/filter?start_date=${startDate}&end_date=${endDate}&city=${city}&category=${category}`);
    const data = await response.json();

    const tableBody = document.getElementById('table-body');
    tableBody.innerHTML = "";  // Clear previous results

    data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${row.ID}</td>
            <td>${row.Date}</td>
            <td>${row.Region}</td>
            <td>${row.City}</td>
            <td>${row.Category}</td>
            <td>${row.Product}</td>
            <td>${row.Qty}</td>
            <td>${row.UnitPrice}</td>
            <td>${row.TotalPrice}</td>
        `;
        tableBody.appendChild(tr);
    });
}

window.onload = loadDropdownOptions;
