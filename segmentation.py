
import duckdb

# Connect to DuckDB. If the database does not exist, it will be created.
con = duckdb.connect(database='transaction.db', read_only=False)


# Execute the SQL statement to create the table


# Verify the table was created by listing tables in the database
tables = con.execute("SHOW TABLES").fetchall()
print(tables)

# Close the connection
con.close()


penguins.head().to_pandas()