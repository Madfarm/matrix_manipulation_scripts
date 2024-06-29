# Using information provided by the web searches and the prompt
average_inc = 81577
avg_monthly_rent = 1300
threshold_for_enough = 0.33

# Calculate monthly income after tax
income_after_tax = (average_inc / 12.0) * 0.82

# Check if the income meets the criter for "enough"
if (avg_monthly_rent / income_after_tax < threshold_for_enough):
    print(f"The average household income in Kansas City is enough for the average rent with the rent being {(avg_monthly_rent / income_after_tax) * 100:.1f}% of monthly income")
else:
    print(f"The average household income in Kansas City is not enough for the average rent with the rent being {(avg_monthly_rent / income_after_tax) * 100:.1f}% of monthly income")

