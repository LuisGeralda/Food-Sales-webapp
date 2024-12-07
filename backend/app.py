from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load Excel data
# Update this file path to point to the actual file location on your system
df = pd.read_excel('backend/sampledatafoodsales_analysis.xlsx', sheet_name='FoodSales')

@app.route('/filter', methods=['GET'])
def filter_data():
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
    # Fetch unique values for City and Category columns for dropdown options
    unique_cities = df['City'].dropna().unique().tolist()
    unique_categories = df['Category'].dropna().unique().tolist()
    return jsonify({'cities': unique_cities, 'categories': unique_categories})

if __name__ == '__main__':
    app.run(debug=True)
