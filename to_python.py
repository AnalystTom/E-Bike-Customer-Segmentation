import duckdb

# Connect to DuckDB. If the database does not exist, it will be created.
con = duckdb.connect(database='transactions.db', read_only=False)

transactions = con.execute("SELECT * FROM transactions").df()
customer = con.execute("SELECT * FROM customers").df()
address = con.execute("SELECT * FROM addresses").df()


print(transactions)

# Close the connection
con.close()