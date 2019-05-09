# read the file containing the prefixes with costs

# using the given phone number, loop through the file containing the prefixes
    # return the price that is attached to the prefiex that matches the phone number 

import os 
from string import find_all_indexes, contains

# # Relative file path
# phone_nums_path = os.path.expanduser('data_csv/phone-numbers-10.txt')
# route_cost_path = os.path.expanduser('data_csv/route-costs-10.txt')

def read_str(file):
    # return contents in file as a list [['prefix, cost'],['prefix, cost']...]
    # return [line.strip().split(",") for line in open(file)]

    dict = {}
    with open(file) as f:
        for line in f:
            (key, value) = line.strip().split(',')
            dict[key] = value
    return dict

def route_cost_check(phone_num: str, route_cost_csv) -> int:
    # open csv file
    prefix_and_route_costs = read_str(route_cost_csv)
    
    # loop through dict
    for prefix in prefix_and_route_costs:
        if prefix in prefix_and_route_costs:
            return prefix_and_route_costs[prefix]
        else:
            return "no price available"
        
        
       
print(route_cost_check('+8614298961866', 'route-costs-35000.txt'))
print(route_cost_check('+1276409','route-costs-35000.txt'))

