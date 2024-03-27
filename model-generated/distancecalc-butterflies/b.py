import math

def calculate_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(waypoints):
    total_distance = 0
    for i in range(len(waypoints) - 1):
        total_distance += calculate_distance(waypoints[i], waypoints[i+1])
    return total_distance

def calculate_time(distance, speed):
    return distance / speed

def calculate_total_time(waypoints, speed):
    total_time = 0
    for i in range(len(waypoints) - 1):
        distance = calculate_distance(waypoints[i], waypoints[i+1])
        time = calculate_time(distance, speed)
        total_time += time
    return total_time

def calculate_travel_time(waypoints):
    return calculate_total_time(waypoints, 25) * 12

def calculate_leap_years(start_year, end_year):
    leap_years = 0
    for year in range(start_year, end_year + 1):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            leap_years += 1
    return leap_years

def calculate_travel_time_with_leap_years(waypoints, start_year, end_year):
    return calculate_travel_time(waypoints) + calculate_leap_years(start_year, end_year) * 24

def main():
    waypoints = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    start_year = 2022
    end_year = 2023
    print("Total distance:", calculate_total_distance(waypoints), "km")
    print("Average speed:", 25, "km/h")
    print("Total travel time:", calculate_travel_time(waypoints), "hours")
    print("Total travel time with leap years:", calculate_travel_time_with_leap_years(waypoints, start_year, end_year), "hours")

if __name__ == "__main__":
    main()