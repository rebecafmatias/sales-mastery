import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

sns.set_theme()

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

merged_df = sales_df.merge(products_df, on='id_product')\
        .merge(customers_df, on='id_customer')\
        [['id_sale','product_name','sale_value',
          'date_reference','name','category']]

merged_df.to_csv('sales_full.csv',index=False)

# Challenge 3 – Total sales per product
# Calculate the total number of sales for each product.
# Also calculate the total sales value per product.
# Identify the best-selling product by quantity.
# Identify the most profitable product (highest total sales value).

sales_qty = sales_df.groupby(['id_product'])['id_product'].count().reset_index(name='count')
sales_value = sales_df.groupby(['id_product'])['id_product'].sum(['sale_value']).reset_index(name='sum')
max_qty_product = sales_qty.nlargest(1,'count')[['id_product']].reset_index(drop=True)
max_profit_product = sales_value.nlargest(1,'sum')[['id_product']].reset_index(drop=True)

# Challenge 4 – Total sales per customer
# Calculate the total amount spent by each customer.
# Find the customer with the highest total spending.
# Create a bar chart (matplotlib or seaborn) showing total purchases per customer.

customer_sales_value = sales_df.groupby(['id_customer'])['id_customer'].sum(['sale_value']).reset_index(name='sum')
customer_highest_total_spending = customer_sales_value.nlargest(1,'sum')[['id_customer']].reset_index(drop=True)

ax = sns.barplot(customer_sales_value,x='id_customer',y='sum')
ax.bar_label(ax.containers[0],fontsize=10)
#plt.show()

# Challenge 5 – Average ticket
# Calculate the average ticket (average sale value across all sales).
# Calculate the average ticket per customer.

avg_ticket = sales_df.agg({'sale_value':'mean'}).to_frame().T
avg_ticket_customerID = sales_df.groupby(['id_customer']).agg({'sale_value':'mean'})
avg_ticket_customer = avg_ticket_customerID.merge(customers_df,on='id_customer')\
    [['id_customer','name','sale_value']]

# Challenge 6 – Value filters
# Create a DataFrame containing only sales above $30.
# Create another DataFrame containing only sales between $20 and $40.

sales_above_30_df = sales_df[sales_df['sale_value']>30]
sales_between_20_40_df = sales_df[(sales_df['sale_value']>=20) & (sales_df['sale_value']<=40)]

# Challenge 7 – Sales by date
# Group sales by date_reference and count the number of sales for each day.
# Create a line chart showing sales trends over time.

sales_by_date_df = sales_df.groupby(['date_reference']).agg({'sale_value':'sum'}).reset_index(names='date_ref')
sales_by_date_chart = sns.relplot(data = sales_by_date_df, kind='line', x='date_ref',y='sale_value')
plt.xticks(rotation=45)  # Rotacionar para não sobrepor
# plt.show()

# Challenge 8 – Sales within a period
# Create a function that receives a start date and end date and returns the total sales value for that period.
# Test the function with the dates 2024-12-05 to 2024-12-12.

def filter_df_by_dates(start_date: str, end_date: str, df: pd.DataFrame, date_col_name: str) -> pd.DataFrame:
    start_date_final = datetime.strptime(start_date,'%Y-%m-%d')
    end_date_final = datetime.strptime(end_date,'%Y-%m-%d')
    df_final_df = df
    df_final_df[date_col_name] = pd.to_datetime(df_final_df[date_col_name])
    sales_filtred_by_date_df = df_final_df[(df_final_df[date_col_name] >= start_date_final) & (df_final_df[date_col_name] <= end_date_final)]
    
    return sales_filtred_by_date_df

filtered_df = filter_df_by_dates('2024-12-05','2024-12-12',sales_df,'date_reference')\
    .sort_values(['date_reference'],ascending=False)

# Challenge 9 – Combined analysis
# Using the combined DataFrame:

# For each category, show the total sales count and total sales value.

# Determine which category generated the most revenue.

# 💡 Extra: Create a script that asks the user (via input()) for a customer’s name and displays:

# Their total purchases

# The products they bought

# Their most recent purchase date


