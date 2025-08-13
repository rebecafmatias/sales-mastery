import pandas as pd

# Challenge 1 – Reading and inspection
# Read each of the three CSV files using pandas (sales.csv, products.csv, customers.csv).
# Display the first 5 rows of each DataFrame.
# Show the total number of rows in each file.

sales_path = '../database/sales.csv'
products_path = '../database/products.csv'
customers_path = '../database/customers.csv'

sales_df = pd.read_csv(sales_path)
products_df = pd.read_csv(products_path)
customers_df = pd.read_csv(customers_path)

def pick_head_df(chosen_df, num_head):
    head_df = chosen_df.head(num_head)
    return head_df

def count_rows_df(chosen_df, id_column):
    qty_rows_df = chosen_df[id_column].count()
    return qty_rows_df


# Challenge 2 – Joining data
# Perform a merge to join sales with products and customers, creating a single DataFrame with:

# Sale ID, product name, sale value, date, customer name, and category.

# Save this combined DataFrame as sales_full.csv.

# Challenge 3 – Total sales per product
# Calculate the total number of sales for each product.

# Also calculate the total sales value per product.

# Identify the best-selling product by quantity.

# Identify the most profitable product (highest total sales value).

# Challenge 4 – Total sales per customer
# Calculate the total amount spent by each customer.

# Find the customer with the highest total spending.

# Create a bar chart (matplotlib or seaborn) showing total purchases per customer.

# Challenge 5 – Average ticket
# Calculate the average ticket (average sale value across all sales).

# Calculate the average ticket per customer.

# Challenge 6 – Value filters
# Create a DataFrame containing only sales above $30.

# Create another DataFrame containing only sales between $20 and $40.

# Challenge 7 – Sales by date
# Group sales by date_reference and count the number of sales for each day.

# Create a line chart showing sales trends over time.

# Challenge 8 – Sales within a period
# Create a function that receives a start date and end date and returns the total sales value for that period.

# Test the function with the dates 2024-12-05 to 2024-12-12.

# Challenge 9 – Combined analysis
# Using the combined DataFrame:

# For each category, show the total sales count and total sales value.

# Determine which category generated the most revenue.

# 💡 Extra: Create a script that asks the user (via input()) for a customer’s name and displays:

# Their total purchases

# The products they bought

# Their most recent purchase date


