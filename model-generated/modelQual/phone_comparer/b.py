def phone_comparer(phones):
    # Calculate the cost-efficiency of each spec
    for phone in phones:
        phone['cost_efficiency'] = {}
        for spec in ['storage', 'battery_life', 'camera']:
            phone['cost_efficiency'][spec] = (phone['price'] / 3) / phone[spec]

    # Sort the phones by cost-efficiency
    phones.sort(key=lambda x: x['cost_efficiency']['storage'] + x['cost_efficiency']['battery_life'] + x['cost_efficiency']['camera'], reverse=True)

    return phones

# Test the tool
phones = [
    {'name': 'Google Pixel 7 Pro', 'price': 1104, 'storage': 14, 'battery_life': 10, 'camera': 14},
    {'name': 'Samsung Galaxy S22 Ultra', 'price': 999, 'storage': 16, 'battery_life': 12, 'camera': 16},
    {'name': 'iPhone 14 Pro', 'price': 999, 'storage': 16, 'battery_life': 12, 'camera': 16}
]

print(phone_comparer(phones))
