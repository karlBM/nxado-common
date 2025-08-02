"""
This module holds needed functions to help with google bigquery
"""
def get_data(spark, dataset, table, limit=None):

    project_id = spark.conf.get("google.cloud.project.id")  # Or set your project ID explicitly

    # Build the table full name
    table_full_name = f"{project_id}.{dataset}.{table}"

    # Read from BigQuery
    df = spark.read \
        .format("bigquery") \
        .option("table", table_full_name) \
        .load()

    # Apply limit if provided
    if limit:
        df = df.limit(limit)

    # Collect results
    results = df.collect()

    # Optional: Convert to list of dicts
    rows = [row.asDict() for row in results]

    spark.stop()

    return rows

# Example usage:
# data = get_data("your_dataset", "your_table", limit=10)
# print(data)
