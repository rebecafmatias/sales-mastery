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
* **Total Sales per period:** Caculate total sales within two dates.

## How to Use

### Prerequisites

* Python 3.6+ installed.
* Basic understanding of Python lists and dictionaries.

### Installation

No specific installation is required for this project. Simply clone the repository or copy the Python script.

### Data Preparation

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
````

### Running the Script

1.  Save the Python script to a file (e.g., `sales_analysis.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using `python sales_analysis.py`.
5.  The results will be printed to the console.

### Example Usage

```python
# Assuming your data is already loaded in the lists 'products', 'sales', and 'customers'

# After running the script, you can access the results like this:

print(f"Most Profitable Product: {most_profitable_product}")
print(f"Highest Spending Customer: {most_profitable_customer}")
print(f"Average Ticket: {avg_ticket}")
print(f"Sales per date: {sales_per_date}")

# To calculate total sales between two dates.
total = calcular_valor_entre_datas('2024-12-01', '2024-12-05')

print(f"Total sales value between the dates is: {total}")

#To view the filtered sales
print(f"sales higher than 25 values:{sales_greater_than_25us}")

#To view all the sales with the costumer info
print(f"sales with costumers info: {sales_list_with_customers_information}")

```

### Output Examples

```
Most Profitable Product: 4
Highest Spending Customer: Joseph
Average Ticket: 31.15
Sales per date: {'2024-12-01': ['1'], '2024-12-02': ['2'], '2024-12-03': ['3'], '2024-12-04': ['4', '5'], '2024-12-05': ['6'], '2024-12-06': ['7'], '2024-12-07': ['8'], '2024-12-08': ['9'], '2024-12-09': ['10'], '2024-12-10': ['11'], '2024-12-11': ['12'], '2024-12-12': ['13'], '2024-12-13': ['14'], '2024-12-14': ['15'], '2024-12-15': ['16'], '2024-12-16': ['17'], '2024-12-17': ['18'], '2024-12-18': ['19'], '2024-12-19': ['20']}
Total sales value between the dates is: 125
sales higher than 25 values: ['2', '4', '7', '8', '9', '11', '12', '13', '15', '16', '17', '19', '20']
sales with costumers info: [{'id_sale': '1', 'id_product': '1', 'sale_value': 20, 'date_reference': '2024-12-01', 'id_customer': '101', 'client_name': 'John', 'client_email': 'john@email.com'}, {'id_sale': '2', 'id_product': '3', 'sale_value': 30, 'date_reference': '2024-12-02', 'id_customer': '102', 'client_name': 'Mary', 'client_email': 'mary@email.com'}, ...etc ]
```

## Contributing

Contributions are welcome\! If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/url?sa=E&source=gmail&q=LICENSE) file for details.
