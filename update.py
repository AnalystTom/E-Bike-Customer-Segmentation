
import duckdb

# Connect to DuckDB. If the database does not exist, it will be created.
con = duckdb.connect(database='transaction.db', read_only=False)

del_row = """
    DELETE FROM customer
    WHERE DOB = "1843-12-21" OR DOB IS NULL;

    DELETE FROM customer
    WHERE product_size_null = NULL;
"""



new_cols_sql = """
    UPDATE transactions
    SET cost = CAST(REPLACE(SUBSTRING(standard_cost, 2), ',', '') AS DECIMAL(10, 2));
    alter table transactions drop column standard_cost;

    UPDATE customer
    SET age = DATE_PART('YEAR', AGE(CURRENT_DATE, DOB));
    alter table transactions drop column DOB;


"""

# converts "standard_cost" to be of the correct format
clean_data_Sql = """
    alter table transactions
    add column if not exists cost decimal(10,2);

    alter table customer
    add column if not exists age integer;
"""

clean_data_Sql = """

    UPDATE customer
        SET gender = CASE
        WHEN gender = 'F' THEN 'Female'
        WHEN gender = 'Femal' THEN 'Female' 
        WHEN gender = 'M' THEN 'Male'
        WHEN gender = 'U' THEN NULL
        ELSE gender
    END;

    UPDATE customer
        SET job_industry_category = "Missing" 
        WHERE job_industry_category IS NULL; 

    UPDATE customer
        SET last_name = "None" 
        WHERE last_name IS NULL; 

    UPDATE customer
        SET job_title = "Missing" 
        WHERE job_title IS NULL; 
        
    UPDATE transactions
        SET online_order = CASE
        WHEN online_order  = NULL THEN 'FALSE'
        ELSE online_order
    END;
"""





# Execute the SQL statement to create the table
con.execute(create_table_sql)

# Verify the table was created by listing tables in the database


# Close the connection
con.close()




