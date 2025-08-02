"""
This module holds needed functions to help with google bigquery
"""
def get_data(spark, dataset, table, limit=None):
    # Assume spark configuration has project ID; otherwise, set explicitly
    project_id = spark.conf.get("google.cloud.project.id", "your-project-id")  # default fallback

    # Build the table full name
    table_full_name = f"{project_id}.{dataset}.{table}"

    # Read from BigQuery
    df = spark.read \
        .format("bigquery") \
        .option("table", table_full_name) \
        .load()

    if limit:
        df = df.limit(limit)

    results = df.collect()

    # Convert to list of dicts
    rows = [row.asDict() for row in results]

    return rows

