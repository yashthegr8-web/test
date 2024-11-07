from flask import Flask, request, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Function to mark attendance in the Excel file
def log_to_excel(timestamp, device_info):
    file_path = "attendance.xlsx"
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        # If no file exists, create a new DataFrame with columns
        df = pd.DataFrame(columns=['User ID', 'Timestamp', 'Device'])

    # Add a new row to the DataFrame
    new_entry = {'User ID': '?', 'Timestamp': timestamp, 'Device': device_info}
    df = df._append(new_entry, ignore_index=True)

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, index=False)

# Route to display the attendance form
@app.route('/')
def submit():
    timestamp = datetime.now()
    ip_address = request.remote_addr  # Fetches the user's IP address

    # Log the data to Excel
    log_to_excel(timestamp, ip_address)

    return "Attendance marked successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
