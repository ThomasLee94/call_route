
from helper import read_str_dict, contains

# ! Overall runtime = O(n)
# ! Overall memory = O(n)
def read_file(file):
    number_list =  []
    with open(file) as f:
        for number in f.read().splitlines():
            number_list.append(number)
    return number_list

def route_cost_check(phone_num: str, prefix_and_route_costs) -> str:
    
    '''cost variable updates as we iteratave over the dicitonary according too
    matching prefix if it is the lowest offset'''

    # This returns a dictionary of the prefixes and the cost as (key, value) pairs
    
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
        return None

    return cost

def lots_of_numbers():
    numbers = read_file('phone-numbers-1000.txt')
    price_list = []
    prefix_and_route_costs = read_str_dict('route-costs-35000.txt') 
    for number in numbers:
        cost = route_cost_check(number, prefix_and_route_costs)
        if cost is not None:
            price_list.append((number, cost))
    return price_list


# numbers = read_file('phone-numbers-1000.txt')
print(lots_of_numbers())
# print(route_cost_check('', 'route-costs-35000.txt'))
# print(read_file('phone-numbers-1000.txt'))

