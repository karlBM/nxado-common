"""
The main entry point for our application
"""
from flask import Request
from gcloud.bigquery import dataset
from pyspark.sql import SparkSession
from nxado.common_bq import get_data

def main(request: Request):
    try:
        spark = SparkSession.builder.getOrCreate()
        request_json = request.get_json()
        if not request_json or 'operation' not in request_json:
            return "Missing 'operation' in request", 400

        operation = request_json['operation']
        table = request_json['table']

        # Dispatch based on operation
        if operation == "get_data":
            result = get_data(spark, dataset, table)
        else:
            return f"Unknown operation: {operation}", 400

        return result

    except Exception as e:
        return f"Error: {str(e)}", 500