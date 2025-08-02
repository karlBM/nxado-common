import os
from flask import Flask, request
from nxado.common_utilities import get_google_credentials, data_request
from pyspark.sql import SparkSession
from nxado.common_bq import get_data
app = Flask(__name__)
spark = SparkSession.builder.getOrCreate()

@app.route('/', methods=['POST'])
def main():
    try:
        request_json = request.get_json()
        if not request_json or 'operation' not in request_json:
            return "Missing 'operation' in request", 400

        result = data_request(request_json)

        return result

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)