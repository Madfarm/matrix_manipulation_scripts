def phone_comparer(phones):
    # Calculate the cost-efficiency of each spec
    for phone in phones:
        phone['cost-efficiency'] = {}
        for spec in phone['specs']:
            if spec != 'price' and spec != 'name':
                cost_efficiency = phone['specs'][spec] / phone['specs']['price']
                phone['cost-efficiency'][spec] = cost_efficiency

    # Sort the phones based on cost-efficiency
    phones.sort(key=lambda x: sum(x['cost-efficiency'].values()), reverse=True)

    return phones

# Example usage
phones = [
    {'name': 'Phone 1', 'price': 1104, 'specs': {'camera': 14, 'battery life': 12, 'storage': 128}},
    {'name': 'Phone 2', 'price': 1000, 'specs': {'camera': 12, 'battery life': 10, 'storage': 64}},
    {'name': 'Phone 3', 'price': 1200, 'specs': {'camera': 16, 'battery life': 15, 'storage': 256}},
]

print(phone_comparer(phones))