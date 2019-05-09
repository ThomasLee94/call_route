
from string import contains

# ! Overall runtime = O(n)
# ! Overall memory = O(n)

def read_str(file):
    # ! Runtime = O(n), n being the number entries in file
    # ! Memory = O(n), n being the number of entries in file

    dict = {}
    with open(file) as f:
        for line in f:
            (key, value) = line.strip().split(',')
            dict[key] = value
    return dict

def route_cost_check(phone_num: str, route_cost_csv) -> str:
    '''cost variable updates as we iteratave over the dicitonary according too
    matching prefix if it is the lowest offset'''

    # This returns a dictionary of the prefixes and the cost as (key, value) pairs
    prefix_and_route_costs = read_str(route_cost_csv) 
    cost = None
    # arbitrary large value for beginning the loop
    old_offset = 2 ** 1000

    # loop through prefix keys in dict
    for prefix in prefix_and_route_costs.keys():
        # ! Runtime = O(n), n being the number of keys in prefix dict
        found = contains(phone_num, prefix)
        if found:
            # the difference between the length of the phone number and the prefix
            offset = len(phone_num) - len(prefix)
            # the lowest difference is the 'correct' match
            if offset <= old_offset:
                # ! Runtime - O(1)
                cost = prefix_and_route_costs[prefix]

    # case: prefix not in dict
    if not cost:
        return 'prefix not in dict'

    return cost
       
print(route_cost_check('+34924199345454', 'route-costs-600.txt'))

