import duckdb

# Connect to DuckDB. If the database does not exist, it will be created.
con = duckdb.connect(database='transaction.db', read_only=False)

# SQL statement to create the 'transactions' table
create_table_sql = """
CREATE TABLE transactions (
    transaction_id INT,
    product_id INT,
    customer_id INT,
    transaction_date DATE,
    online_order BOOLEAN,
    order_status VARCHAR,
    brand VARCHAR,
    product_line VARCHAR,
    product_class VARCHAR,
    product_size VARCHAR,
    list_price FLOAT,
    standard_cost FLOAT,
    product_first_sold_date INT
    );

    CREATE TABLE customers (
    customer_id INT, 
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    past_3_years_bike_related_purchases INT,
    DOB DATE,
    job_title VARCHAR,
    job_industry VARCHAR,
    wealth_segment VARCHAR,
    deceased_indicator VARCHAR,
    owns_car VARCHAR,
    tenure INT
    );

    CREATE TABLE addresses (
    customer_id INT,
    address VARCHAR,
    postcode INT,
    state VARCHAR,
    country VARCHAR,
    property_valuation INT
    );

"""

# Execute the SQL statement to create the table
con.execute(create_table_sql)

# Verify the table was created by listing tables in the database
tables = con.execute("SHOW TABLES").fetchall()
print(tables)

# Close the connection
con.close()