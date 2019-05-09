# read the file containing the prefixes with costs

# using the given phone number, loop through the file containing the prefixes
    # return the price that is attached to the prefiex that matches the phone number 

import os 

# Relative file path
phone_nums_path = os.path.expanduser('data_csv/phone-numbers-10.txt')
route_cost_path = os.path.expanduser('data_csv/route-costs-10.txt')

def read_str_tuple(file):
    # return contents in file as a tuple
    return (line.strip() for line in open(file))
    # return ((prefix, cost),(prefix, cost)...)

def route_cost_check(phone_num, route_cost_csv) -> int:
    # prefix + number
    phone_num_prefix = 
    # open csv file
    prefix_and_route_costs = read_str_tuple(route_cost_csv)
    
    # loop through prefix_and_route_costs
        # return second element of tuple
