import duckdb

# Connect to DuckDB. If the database does not exist, it will be created.
con = duckdb.connect(database='transactions.db', read_only=False)

# Delete rows based on conditions
del_row_sql = """
DELETE FROM customers WHERE DOB = '1843-12-21' OR DOB IS NULL;
"""
con.execute(del_row_sql)

# Correctly handling comparison with NULL
update_online_order_sql = """
UPDATE transactions SET online_order = CASE WHEN online_order IS NULL THEN 'FALSE' ELSE online_order END;
"""
con.execute(update_online_order_sql)

# Preparing for data cleanup and transformations
prepare_columns_sql = """
ALTER TABLE transactions ADD COLUMN IF NOT EXISTS cost DECIMAL(10,2);
ALTER TABLE customers ADD COLUMN IF NOT EXISTS age INTEGER;
"""
con.execute(prepare_columns_sql)

# Data cleanup and transformations
clean_data_sql = """
UPDATE transactions SET cost = CAST(REPLACE(SUBSTRING(standard_cost, 2), ',', '') AS DECIMAL(10, 2));
UPDATE customers SET age = DATE_PART('year', CURRENT_TIMESTAMP) - DATE_PART('year', CAST(DOB AS DATE));
"""
con.execute(clean_data_sql)

# Drop the columns after their data has been used or transformed
drop_columns_sql = """
ALTER TABLE transactions DROP COLUMN standard_cost;
ALTER TABLE customers DROP COLUMN DOB;
"""
con.execute(drop_columns_sql)

# Updating customer information based on various conditions
update_customer_info_sql = """
UPDATE customers
SET gender = CASE
    WHEN gender = 'F' THEN 'Female'
    WHEN gender = 'Femal' THEN 'Female' 
    WHEN gender = 'M' THEN 'Male'
    WHEN gender = 'U' THEN NULL
    ELSE gender
END;

UPDATE customers SET job_industry_category = 'Missing' WHERE job_industry_category IS NULL; 
UPDATE customers SET last_name = 'None' WHERE last_name IS NULL; 
UPDATE customers SET job_title = 'Missing' WHERE job_title IS NULL;
"""
con.execute(update_customer_info_sql)

# Close the connection
con.close()



