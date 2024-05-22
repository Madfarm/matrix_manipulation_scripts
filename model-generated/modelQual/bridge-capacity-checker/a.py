def can_handle_weight(weight_capacity, vehicles):
    total_weight = sum(vehicles)
    if total_weight <= weight_capacity:
        return True
    else:
        return False

# example usage
weight_capacity = 80000  # in pounds
vehicles = [10000, 20000, 30000]  # weights of vehicles in pounds
print(can_handle_weight(weight_capacity, vehicles))