
from string import contains
from find_all_prefixes import find_index

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
    # This returns a dictionary of the prefixes and the cost as (key, value) pairs
    prefix_and_route_costs = read_str(route_cost_csv) 
    '''cost variable updates as we iteratave over the dicitonary according too
        matching prefix if it is the lowest offset'''
    cost = None
    # counter to have end state if prefix is not found in dict
    counter = 0 
    # arbitrary large value for beginning the loop
    old_offset = 99999
    for prefix in prefix_and_route_costs.keys():
        # found = find_index(phone_num, prefix)
        found = contains(phone_num, prefix)
        if found:
            # the difference between the length of the phone number and the prefix
            offset = len(phone_num) - len(prefix)
            # the lowest difference is the 'correct' match
            if offset <= old_offset:
                # look up cost in dict for constant look up time
                cost = prefix_and_route_costs[prefix]
        counter += 1
    # case: prefix not in dict
    if not cost:
        return 'prefix not in dict'
    return cost

    
        

       
print(route_cost_check('+34924199345454', 'route-costs-600.txt'))
# print(route_cost_check('+1276409','route-costs-600.txt'))

