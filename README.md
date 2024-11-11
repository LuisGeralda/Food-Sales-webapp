# Food Sales Analysis Web App

This is a simple, responsive web application to analyze food sales data. Users can filter sales records by date, city, and category, with results displayed in a clean, tabulated format. The frontend is designed with an Apple-inspired aesthetic, featuring a modern gradient background and responsive design.

## Features
Filter data by date range, city, and category.
Display results in a tabulated, aesthetically pleasing format.
Responsive design for compatibility with different screen sizes.
Backend built with Flask for data handling and filtering.
Frontend built with HTML, CSS, and JavaScript.

## Technologies Used
Backend: Python, Flask, Pandas

Frontend: HTML, CSS, JavaScript

Server: Apache (via XAMPP or WAMP for local development)

## Setup Instructions

### Clone the Repository:
```
git clone https://github.com/your-username/food-sales-analysis.git
cd food-sales-analysis
```

### Install Dependencies:

Make sure you have Python and pip installed, then install the necessary Python packages:
```
pip install flask pandas flask-cors
```
### Start the Flask Backend: 

Run the app.py file to start the backend server.
```
python backend/app.py
```
### Set Up the Frontend:

1. Install and start Apache via XAMPP or WAMP.

2. Place the frontend files in the Apache htdocs folder for local access.
  
3. Access the frontend at `http://localhost/foodsales/index.html` 

### Access the Application:

Open your browser and go to `http://localhost/foodsales/index.html`.

Use the filter options to view food sales data based on your criteria.
