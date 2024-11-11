// File: script.js
// Ensure URLs point to the Flask backend on http://127.0.0.1:5000

// Fetch unique values for dropdowns
async function loadDropdownOptions() {
    const response = await fetch('http://127.0.0.1:5000/unique-values');
    const data = await response.json();

    // Populate City dropdown
    const cityDropdown = document.getElementById('city');
    data.cities.forEach(city => {
        const option = document.createElement('option');
        option.value = city;
        option.text = city;
        cityDropdown.add(option);
    });

    // Populate Category dropdown
    const categoryDropdown = document.getElementById('category');
    data.categories.forEach(category => {
        const option = document.createElement('option');
        option.value = category;
        option.text = category;
        categoryDropdown.add(option);
    });
}

// Fetch filtered data based on user input
async function fetchData() {
    const startDate = document.getElementById('start-date').value;
    const endDate = document.getElementById('end-date').value;
    const city = document.getElementById('city').value;
    const category = document.getElementById('category').value;

    const response = await fetch(`http://127.0.0.1:5000/filter?start_date=${startDate}&end_date=${endDate}&city=${city}&category=${category}`);
    const data = await response.json();

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = JSON.stringify(data, null, 2);
}

// Load dropdown options on page load
window.onload = loadDropdownOptions;
