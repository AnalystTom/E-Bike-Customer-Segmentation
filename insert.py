import duckdb
import pandas as pd

# Define the CSV file paths
csv_files = {
    'transactions': 'data/transactions.csv',
    'customers': 'data/clients.csv',
    'addresses': 'data/addresses.csv',
}

# Connect to the DuckDB database
con = duckdb.connect(database='transactions.db', read_only=False)

# Loop through each table and corresponding CSV file
for table_name, file_path in csv_files.items():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Use DuckDB's functionality to insert the DataFrame directly into the table
    # This creates the table if it doesn't exist, or inserts into it if it does
    con.register(table_name, df)
    con.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM {table_name};")
    # Unregister to free up the namespace
    con.unregister(table_name)

# Commit changes and close the connection
con.close()