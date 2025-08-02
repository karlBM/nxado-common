"""
The main entry point for our application
"""
from flask import Request
from pyspark.sql import SparkSession


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    spark = SparkSession.builder \
        .appName("BigQueryQuery") \
        .getOrCreate()

    request_json = request.get_json()

    # Get the operation name
    operation = request_json.get("operation")

    # Call different functions based on the operation
    if operation == "op_a":
        result = function_a()
    elif operation == "op_b":
        result = function_b()
    elif operation == "op_c":
        result = function_c()
    else:
        return "Invalid operation", 400

    return result

    get_data(spark, dataset, table, limit=None)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
