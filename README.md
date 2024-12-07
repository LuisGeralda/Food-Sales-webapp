# Food Sales Analysis Web App

This is a simple, responsive web application to analyze food sales data. Users can filter sales records by date, city, and category, with results displayed in a clean, tabulated format. The frontend is designed with an Apple-inspired aesthetic, featuring a modern gradient background and responsive design.

## Features
- Filter data by date range, city, and category.
- Display results in a tabulated, aesthetically pleasing format.
- Responsive design for compatibility with different screen sizes.
- Backend built with Flask for data handling and filtering.
- Frontend built with HTML, CSS, and JavaScript.

## Technologies Used
- **Backend**: Python, Flask, Pandas
- **Frontend**: HTML, CSS, JavaScript
- **Server**: Apache (via XAMPP or WAMP for local development)

## Setup Instructions

### Clone the Repository:
```
git clone https://github.com/LuisGeralda/Food-Sales-webapp.git
cd food-sales-analysis
```

### Install Dependencies:

Make sure you have Python and pip installed, then install the necessary Python packages:
```
pip install flask pandas flask-cors
```

### Start the Flask Backend:

Run the `app.py` file to start the backend server.
```
python backend/app.py
```

### Deploying on Render:

To deploy the application on Render:

1. **Prepare the Repository:**
   - Ensure the project structure is as follows:
     ```
     project/
     ├── backend/
     │   ├── app.py
     │   └── sampledatafoodsales_analysis.xlsx
     ├── frontend/
     │   ├── index.html
     │   ├── styles.css
     │   ├── script.js
     ├── requirements.txt
     ```
   - Push the repository to GitHub.

2. **Set Up a Render Account:**
   - Log in to [Render](https://render.com/) and create a new web service.

3. **Connect the Repository:**
   - Link your GitHub repository to Render.

4. **Configure the Service:**
   - Use `python backend/app.py` as the start command.
   - Ensure the `PORT` environment variable is set by Render.

5. **Deploy the Application:**
   - Render will automatically detect the changes and deploy the app.

6. **Access the Application:**
   - Visit the live Render URL (e.g., `https://food-sales-webapp.onrender.com`) to access the web app.

### Access the Application Locally:

For local development:

1. **Set Up the Frontend:**
   - Install and start Apache via XAMPP or WAMP.
   - Place the frontend files in the Apache `htdocs` folder for local access.

2. **Access the Frontend:**
   - Open your browser and go to `http://localhost/foodsales/index.html`.

3. **Test the Backend:**
   - Ensure the Flask backend is running.
   - Use the filter options to view food sales data based on your criteria.

---

Enjoy exploring food sales data with this intuitive web application!

