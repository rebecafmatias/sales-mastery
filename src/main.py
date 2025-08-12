products = [
    {'id_product': '1', 'product_name': 'dress', 'brand': 'x', 'unit_value': 20, 'category': 'clothing'},
    {'id_product': '2', 'product_name': 'shirt', 'brand': 'y', 'unit_value': 25, 'category': 'clothing'},
    {'id_product': '3', 'product_name': 'pants', 'brand': 'z', 'unit_value': 30, 'category': 'clothing'},
    {'id_product': '4', 'product_name': 'shoes', 'brand': 'w', 'unit_value': 50, 'category': 'shoes'},
]

sales = [
    {'id_sale': '1', 'id_product': '1', 'sale_value': 20, 'date_reference': '2024-12-01', 'id_customer': '101'},
    {'id_sale': '2', 'id_product': '3', 'sale_value': 30, 'date_reference': '2024-12-02', 'id_customer': '102'},
    {'id_sale': '3', 'id_product': '1', 'sale_value': 20, 'date_reference': '2024-12-03', 'id_customer': '101'},
    {'id_sale': '4', 'id_product': '4', 'sale_value': 50, 'date_reference': '2024-12-04', 'id_customer': '103'},
    {'id_sale': '5', 'id_product': '2', 'sale_value': 25, 'date_reference': '2024-12-04', 'id_customer': '104'},
    {'id_sale': '6', 'id_product': '1', 'sale_value': 15, 'date_reference': '2024-12-05', 'id_customer': '101'},
    {'id_sale': '7', 'id_product': '3', 'sale_value': 35, 'date_reference': '2024-12-06', 'id_customer': '102'},
    {'id_sale': '8', 'id_product': '4', 'sale_value': 45, 'date_reference': '2024-12-07', 'id_customer': '103'},
    {'id_sale': '9', 'id_product': '2', 'sale_value': 30, 'date_reference': '2024-12-08', 'id_customer': '104'},
    {'id_sale': '10', 'id_product': '1', 'sale_value': 22, 'date_reference': '2024-12-09', 'id_customer': '101'},
    {'id_sale': '11', 'id_product': '3', 'sale_value': 28, 'date_reference': '2024-12-10', 'id_customer': '102'},
    {'id_sale': '12', 'id_product': '4', 'sale_value': 55, 'date_reference': '2024-12-11', 'id_customer': '103'},
    {'id_sale': '13', 'id_product': '2', 'sale_value': 27, 'date_reference': '2024-12-12', 'id_customer': '104'},
    {'id_sale': '14', 'id_product': '1', 'sale_value': 18, 'date_reference': '2024-12-13', 'id_customer': '101'},
    {'id_sale': '15', 'id_product': '3', 'sale_value': 32, 'date_reference': '2024-12-14', 'id_customer': '102'},
    {'id_sale': '16', 'id_product': '4', 'sale_value': 48, 'date_reference': '2024-12-15', 'id_customer': '103'},
    {'id_sale': '17', 'id_product': '2', 'sale_value': 29, 'date_reference': '2024-12-16', 'id_customer': '104'},
    {'id_sale': '18', 'id_product': '1', 'sale_value': 21, 'date_reference': '2024-12-17', 'id_customer': '101'},
    {'id_sale': '19', 'id_product': '3', 'sale_value': 31, 'date_reference': '2024-12-18', 'id_customer': '102'},
    {'id_sale': '20', 'id_product': '4', 'sale_value': 49, 'date_reference': '2024-12-19', 'id_customer': '103'},
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
            break
        sales_list_with_cat_and_prod.append(sales_dict_with_cat_and_prod)

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

# Calculate the average ticket per sale:
# Calculate the average value of sales made.

qty_sales = 0
total_sales_value = 0
current_sale = ''
sales_determined = []

for i in sales:
    current_sale = i['id_sale']
    if current_sale not in sales_determined:
        sales_determined.append(current_sale)
        qty_sales += 1
        total_sales_value += i['sale_value']

avg_ticket = total_sales_value/qty_sales
    

# Find sales above a certain value:
# Create a list with sales that had a value greater than a certain value (e.g., $30).

sales_greater_than_25us = []

for i in sales:
    id_sale = i['id_sale']
    if i['sale_value'] > 25:
        sales_greater_than_25us.append(id_sale)

# Group sales by date:
# Create a dictionary where the keys are the dates and the values are lists of sales made on that date.

# {'2024-01-01': [x,y,z], '2024-01-02': [a,b,c]}

sales_per_date = {}

for i in sales:
    date_reference = i['date_reference']
    id_sale = i['id_sale']
    if date_reference in sales_per_date:
        sales_per_date.get(date_reference).append(id_sale)
    elif date_reference not in sales_per_date:
        sales_per_date.update({date_reference: [id_sale]})

# Calculate total sales per period:
# Calculate total sales in a given period (e.g., between two dates). 

def calcular_valor_entre_datas(initial_datetime, end_datetime):

    from datetime import datetime


    total_sales_per_period = 0

    for i in sales:
        initial_datetime = datetime.strptime(initial_datetime, "%Y-%m-%d")
        end_datetime = datetime.strptime(end_datetime, "%Y-%m-%d")
        date_reference = datetime.strptime(i['date_reference'], "%Y-%m-%d")

        sale_value = i['sale_value']

        if date_reference >= initial_datetime and date_reference <= end_datetime:
            total_sales_per_period += sale_value
            break
    return total_sales_per_period


# result = calcular_valor_entre_datas(
#     input('Start Date: '),
#     input('End Date: ')
# )


# Add customer information to sales:
# Create a new list of sales that includes customer data (name, email) for each sale.

sales_list_with_customers_information = []
sales_dic_with_customers_information = {}

for i in sales:
    sales_dic_with_customers_information = i
    id_customer = i['id_customer']
    for j in customers:
        client_name = j['name']
        client_email = j['email']
        if id_customer == j['id_customer']:
            sales_dic_with_customers_information.update({'client_name': client_name, 'client_email': client_email})
            sales_list_with_customers_information.append(sales_dic_with_customers_information)
