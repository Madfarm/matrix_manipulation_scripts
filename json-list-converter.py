listicle = [
    {
        "user_count": 1,
        "start_date:month": "April 2023",
        "odoo_instance_plan_id": [
            1,
            "Luxury Plan"
        ],
    },
    {
        "user_count": 2,
        "start_date:month": "May 2023",
        "odoo_instance_plan_id": [
            1,
            "Luxury Plan"
        ],
    },
    {
        "user_count": 1,
        "start_date:month": "May 2023",
        "odoo_instance_plan_id": [
            6,
            "Pro Vip"
        ],
    },
]



# Initialize the dictionary
result = {
    'labels': [],
    'datasets': []
}

# Iterate over the list
for item in listicle:

    # Get the month
    month = item['start_date:month']

    # Add the month to the labels list
    if month not in result['labels']:
        result['labels'].append(month)

    # Get the plan ID
    plan_id = item['odoo_instance_plan_id'][0]

    # Get the plan name
    plan_name = item['odoo_instance_plan_id'][1]

    # Check if the plan exists in the datasets list
    if plan_id not in [dataset['label'] for dataset in result['datasets']]:

        # Add the plan to the datasets list
        result['datasets'].append({
            'label': plan_name,
            'data': []
        })

    # Add the user count to the plan's data list
    result['datasets'][-1]['data'].append(item['user_count'])

# Print the result
print(result)