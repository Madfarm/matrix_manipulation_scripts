import statistics
from scipy.stats import shapiro


def analyze_sales_data(sales_data):
    assert len(sales_data) == 12, "The data set must contain 12 numbers."


    # Calculate the total sales for the year
    total_sales = sum(sales_data)
    print(f"Total sales for the year: {total_sales}")


    # Determine the monthly average sales
    monthly_average_sales = total_sales / len(sales_data)
    print(f"Monthly average sales: {monthly_average_sales}")


    # Identify the month with the highest sales
    max_sales = max(sales_data)
    max_sales_month = sales_data.index(max_sales) + 1
    print(f"The month with the highest sales is month {max_sales_month} with {max_sales} sales.")


    # Find the month-to-month percentage change in sales
    for i in range(1, len(sales_data)):
        previous_month_sales = sales_data[i - 1]
        current_month_sales = sales_data[i]
        percentage_change = (current_month_sales - previous_month_sales) / previous_month_sales * 100
        print(f"The month-to-month percentage change from month {i} to month {i+1} is {percentage_change}%.")


    # Test whether the sales data follow a normal distribution using a Shapiro-Wilk test
    _, p_value = shapiro(sales_data)
    if p_value > 0.05:
        print("The sales data follow a normal distribution.")
    else:
        print("The sales data do not follow a normal distribution.")


sales_data = [10000, 12000, 11000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]
analyze_sales_data(sales_data)