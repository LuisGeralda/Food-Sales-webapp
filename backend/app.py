from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os
import logging

# Configure the Flask app
app = Flask(__name__, static_folder='frontend')
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Load Excel data
try:
    df = pd.read_excel('backend/sampledatafoodsales_analysis.xlsx', sheet_name='FoodSales')
    logger.info("Excel file loaded successfully.")
except FileNotFoundError:
    df = None
    logger.error("Error: Excel file not found. Ensure 'sampledatafoodsales_analysis.xlsx' is in the correct path.")

@app.route('/')
def serve_frontend():
    logger.info("Serving index.html for the root URL.")
    # Serve the main frontend page (index.html)
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    logger.info(f"Serving static file: {path}")
    # Serve other static files such as styles.css and script.js
    return send_from_directory(app.static_folder, path)

@app.route('/filter', methods=['GET'])
def filter_data():
    if df is None:
        logger.error("Data not loaded. Excel file is missing.")
        return jsonify({"error": "Data not loaded. Ensure the Excel file is present."}), 500

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    city = request.args.get('city')
    category = request.args.get('category')

    logger.info(f"Filtering data with parameters - Start Date: {start_date}, End Date: {end_date}, City: {city}, Category: {category}")

    # Convert date columns to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%d-%b')

    # Filter data
    filtered_df = df
    if start_date and end_date:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        filtered_df = filtered_df[(filtered_df['Date'] >= start_date) & (filtered_df['Date'] <= end_date)]
    if city:
        filtered_df = filtered_df[filtered_df['City'] == city]
    if category:
        filtered_df = filtered_df[filtered_df['Category'] == category]

    logger.info(f"Filtered data contains {len(filtered_df)} rows.")
    return jsonify(filtered_df.to_dict(orient='records'))

@app.route('/unique-values', methods=['GET'])
def unique_values():
    if df is None:
        logger.error("Data not loaded. Excel file is missing.")
        return jsonify({"error": "Data not loaded. Ensure the Excel file is present."}), 500

    # Fetch unique values for City and Category columns for dropdown options
    unique_cities = df['City'].dropna().unique().tolist()
    unique_categories = df['Category'].dropna().unique().tolist()

    logger.info(f"Unique values fetched - Cities: {len(unique_cities)}, Categories: {len(unique_categories)}")
    return jsonify({'cities': unique_cities, 'categories': unique_categories})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting the app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
