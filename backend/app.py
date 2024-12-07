from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__, static_folder='frontend')
CORS(app)

# Load Excel data
try:
    df = pd.read_excel('backend/sampledatafoodsales_analysis.xlsx', sheet_name='FoodSales')
except FileNotFoundError:
    df = None
    print("Error: Excel file not found. Ensure 'sampledatafoodsales_analysis.xlsx' is in the correct path.")

@app.route('/frontend/')
def serve_frontend():
    # Serve the index.html file from the frontend folder
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/filter', methods=['GET'])
def filter_data():
    if df is None:
        return jsonify({"error": "Data not loaded. Ensure the Excel file is present."}), 500

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    city = request.args.get('city')
    category = request.args.get('category')

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

    return jsonify(filtered_df.to_dict(orient='records'))

@app.route('/unique-values', methods=['GET'])
def unique_values():
    if df is None:
        return jsonify({"error": "Data not loaded. Ensure the Excel file is present."}), 500

    # Fetch unique values for City and Category columns for dropdown options
    unique_cities = df['City'].dropna().unique().tolist()
    unique_categories = df['Category'].dropna().unique().tolist()
    return jsonify({'cities': unique_cities, 'categories': unique_categories})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
