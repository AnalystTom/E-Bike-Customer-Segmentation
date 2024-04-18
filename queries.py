import duckdb

# Connect to DuckDB. If the database does not exist, it will be created.
con = duckdb.connect(database='transaction.db', read_only=False)

# SQL statement to create the 'transactions' table
create_table_sql = """
    SELECT * FROM transactions;

"""

# Execute the SQL statement to create the table
con.execute(create_table_sql)

# Verify the table was created by listing tables in the database


# Close the connection
con.close()