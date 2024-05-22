def check_weight_capacity(bridge_capacity, vehicle_weights):
    total_weight = sum(vehicle_weights)
    if total_weight > bridge_capacity:
        return False
    else:
        return True

# Test the function
bridge_capacity = 80000  # weight capacity of the bridge in pounds
vehicle_weights = [20000, 15000, 30000, 25000]  # weights of vehicles in pounds
print(check_weight_capacity(bridge_capacity, vehicle_weights))