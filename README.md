![Sales Mastery](sales_pic.png)

# Sales Mastery

## Description

This project provides a comprehensive sales analysis using Python, offering valuable insights into product performance, customer behavior, and overall sales trends. It leverages structured data to perform various calculations and generate reports, empowering businesses to make data-driven decisions.

## Features

* **Total Sales per Product:** Calculate and display the total sales for each product, allowing for identification of top-performing items.
* **Most Profitable Product:** Determine the product that generated the highest revenue.
* **Sales Analysis per Customer:** Analyze customer purchase patterns and identify high-value clients.
* **Highest Spending Customer:** Pinpoint the customer with the highest total purchase value.
* **Average Ticket Calculation:** Calculate the average sales transaction value.
* **Sales Grouped by Date:** Organize sales data by date to visualize trends over time.
* **Comprehensive Sales Report:** Generate a detailed report encompassing all sales information, including customer and product data.
* **Sales above a certain value:** Filter sales that are above a certain value.
* **Total Sales per period:** Calculate total sales within two dates.

## Data Preparation

The project requires sales, products, and customers data in the following format:

```python
products = [
    {'id_product': '1', 'product_name': 'dress', 'brand': 'x', 'unit_value': 20, 'category': 'clothing'},
    # ... more products
]

sales = [
    {'id_sale': '1', 'id_product': '1', 'sale_value': 20, 'date_reference': '2024-12-01', 'id_customer': '101'},
    # ... more sales
]

customers = [
    {'id_customer': '101', 'name': 'John', 'email': 'john@email.com', 'phone': '11999999999', 'address': 'Example Street, 123'},
    # ... more customers
]
```

## Installation

This project uses **Poetry** to manage dependencies.  

1. Install Poetry if you don't have it:
```bash
pip install poetry
```

2. Install project dependencies:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

## Running the Script

1. Save the Python script (`sales_file_analysis.py`) in your project folder.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using:
```bash
python sales_file_analysis.py
```
5. The results will be printed to the console.

## Example Usage

```python
# Assuming your data is already loaded in the lists 'products', 'sales', and 'customers'

print(f"Most Profitable Product: {most_profitable_product}")
print(f"Highest Spending Customer: {most_profitable_customer}")
print(f"Average Ticket: {avg_ticket}")
print(f"Sales per date: {sales_per_date}")

# To calculate total sales between two dates
total = calcular_valor_entre_datas('2024-12-01', '2024-12-05')
print(f"Total sales value between the dates is: {total}")

# To view filtered sales
print(f"Sales higher than 25: {sales_greater_than_25us}")

# To view all sales with customer info
print(f"Sales with customer info: {sales_list_with_customers_information}")
```

## Example Output

```
Most Profitable Product: 4
Highest Spending Customer: Joseph
Average Ticket: 31.15
Sales per date: {'2024-12-01': ['1'], '2024-12-02': ['2'], ...}
Total sales value between the dates is: 125
Sales higher than 25: ['2', '4', '7', '8', ...]
Sales with customer info: [{'id_sale': '1', 'id_product': '1', 'sale_value': 20, 'date_reference': '2024-12-01', 'id_customer': '101', 'client_name': 'John', 'client_email': 'john@email.com'}, ...]
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.

## License

This project is open-source and available for personal and educational use.

