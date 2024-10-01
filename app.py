from flask import Flask, jsonify
import pandas as pd
import DE_function
import json
 
# Assuming your DataFrame is named df
# Load your DataFrame here
df = DE_function.getdf()
 
app = Flask(__name__)
 
@app.route('/are154/dataapi', methods=['GET'])
def get_table():
    # Convert DataFrame to JSON
    json_data = df.to_dict(orient = "records")
    return jsonify(json_data)



with open('metadata.json') as json_file:
    data = json.load(json_file)

@app.route('/are154/dataapi/metadata', methods=['GET'])
def get_metadata():
    return jsonify(data)
 
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
