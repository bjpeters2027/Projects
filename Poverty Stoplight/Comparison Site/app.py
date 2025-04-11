from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load JSON data files (make sure they are in the same directory as app.py)
with open('MPI.json', 'r') as mpi_file:
    mpi_data = json.load(mpi_file)

with open('comparison.json', 'r') as comp_file:
    comp_data = json.load(comp_file)

# List of attributes to compare
ATTRIBUTES = ["education", "electricity", "sanitation", "water", "housing", "assets"]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    key = None
    if request.method == 'POST':
        # Get the key from the form input.
        key = request.form.get('key')
        if key:
            if key in mpi_data and key in comp_data:
                mpi_entry = mpi_data[key]
                comp_entry = comp_data[key]
                # Build a result dictionary with attribute comparisons, descriptions, and the MPI label.
                result = {
                    'mpi_attributes': {attr: mpi_entry.get(attr, 'N/A') for attr in ATTRIBUTES},
                    'comp_attributes': {attr: comp_entry.get(attr, 'N/A') for attr in ATTRIBUTES},
                    'mpi_description': mpi_entry.get('description', 'No description available'),
                    'comp_description': comp_entry.get('description', 'No description available'),
                    'mpi_label': mpi_entry.get('label', 'N/A')
                }
            else:
                error = f"Key {key} not found in one or both files."
        else:
            error = "Please enter a key."
    return render_template("index.html", result=result, error=error, key=key)


if __name__ == '__main__':
    # Run the app on localhost port 5000
    app.run(debug=True)
