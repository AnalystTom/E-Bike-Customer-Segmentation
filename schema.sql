CREATE TABLE tranasactions (
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
)

CREATE TABLE customer (
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
    tenure INT,
)

CREATE TABLE address (
    customer_id INT,
    address VARCHAR,
    postcode INT,
    state VARCHAR,
    country VARCHAR,
    property_valuation INT,
)