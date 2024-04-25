import duckdb

# Connect to DuckDB. If the database does not exist, it will be created.
con = duckdb.connect(database='transaction.db', read_only=False)

# SQL statement to calculate customers per postcode
Postcode_metrics = """
    CREATE OR REPLACE VIEW v1 AS
    SELECT SUM(customer_id)
    FROM customers
    JOIN addresses ON customers.customer_id = addresses.customer_id
    GROUP BY addresses.postcode;
"""

# Close the connection
con.close()