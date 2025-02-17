products = [
    {'id_product': '1', 'product_name': 'dress', 'brand': 'x', 'unit_value': 20, 'category': 'clothing'},
    {'id_product': '2', 'product_name': 'shirt', 'brand': 'y', 'unit_value': 25, 'category': 'clothing'},
    {'id_product': '3', 'product_name': 'pants', 'brand': 'z', 'unit_value': 30, 'category': 'clothing'},
    {'id_product': '4', 'product_name': 'shoes', 'brand': 'w', 'unit_value': 50, 'category': 'shoes'},
]

sales = [
    {'id_sale': '1', 'id_product': '1', 'sale_value': 20, 'date_reference': '2024-12-04', 'id_customer': '101'},
    {'id_sale': '2', 'id_product': '3', 'sale_value': 30, 'date_reference': '2024-12-04', 'id_customer': '102'},
    {'id_sale': '3', 'id_product': '1', 'sale_value': 20, 'date_reference': '2024-12-05', 'id_customer': '101'},
    {'id_sale': '4', 'id_product': '4', 'sale_value': 50, 'date_reference': '2024-12-05', 'id_customer': '103'},
]

customers = [
    {'id_customer': '101', 'name': 'John', 'email': 'john@email.com', 'phone': '11999999999', 'address': 'Example Street, 123'},
    {'id_customer': '102', 'name': 'Mary', 'email': 'mary@email.com', 'phone': '11888888888', 'address': 'Example Avenue, 456'},
    {'id_customer': '103', 'name': 'Joseph', 'email': 'joseph@email.com', 'phone': '11777777777', 'address': 'Example Square, 789'},
]

# Create a dictionary that stores the total sales for each product,
# using the product name as the key and the total as the value.

sales_list_with_cat_and_prod = []
sales_dict_with_cat_and_prod = {}
sales_by_product_dict = {}

for sale in sales:
    id_product = sale['id_product']
    sales_dict_with_cat_and_prod = sale
    for product in products:
        if id_product == product['id_product']:
            sales_dict_with_cat_and_prod.update(
                {
                    'product_category': product['category'],
                    'product_name': product['product_name']
                }
            )
        sales_list_with_cat_and_prod.append(sales_dict_with_cat_and_prod)
        break

for item in sales_list_with_cat_and_prod:
    product_name = item['product_name']
    if product_name in sales_by_product_dict:
        sales_by_product_dict[product_name] += 1
    elif product_name not in sales_by_product_dict:
        sales_by_product_dict.update({product_name: 1})

# Discover which product had the highest total sales value.

value_sale_by_prod_dict = {}

for item in sales_list_with_cat_and_prod:
    id_product = item['id_product']
    sale_value = item['sale_value']
    if id_product in value_sale_by_prod_dict:
        value_sale_by_prod_dict[id_product] += sale_value
    elif id_product not in value_sale_by_prod_dict:
        value_sale_by_prod_dict.update({id_product: sale_value})

most_profitable_product = max(value_sale_by_prod_dict, key=value_sale_by_prod_dict.get)

# Create a dictionary that stores the total sales for each customer,
# using the customer name as the key and the total as the value.
# Discover which customer had the highest total purchase value.

sales_with_customers_list = []
sales_with_customers_dict = {}
sales_by_customer = {}

for sale in sales:
    customer_id = sale['id_customer']
    sales_with_customers_dict = sale
    for customer in customers:
        if customer['id_customer'] == customer_id:
            sales_with_customers_dict.update({'customer_name': customer['name']})
            sales_with_customers_list.append(sales_with_customers_dict)
            break

for item in sales_with_customers_list:
    customer_name = item['customer_name']
    sale_value = item['sale_value']
    if customer_name in sales_by_customer:
        sales_by_customer[customer_name] += sale_value
    elif customer_name not in sales_by_customer:
        sales_by_customer.update({customer_name: sale_value})

most_profitable_customer = max(sales_by_customer, key=sales_by_customer.get)

# 5. Calculate the average ticket per sale:
# Calculate the average value of sales made.

# 6. Find sales above a certain value:
# Create a list with sales that had a value greater than a certain value (e.g., $30).

# 7. Group sales by date:
# Create a dictionary where the keys are the dates and the values are lists of sales made on that date.

# 8. Calculate total sales per period:
# Calculate total sales in a given period (e.g., between two dates).

# 9. Add customer information to sales:
# Create a new list of sales that includes customer data (name, email) for each sale.

# 10. Create a complete sales report:
# Create a report that includes all relevant information about sales, such as date, product, customer, value, etc.