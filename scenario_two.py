from scenario_one import route_cost_check


def get_numbers_list(file):
    numbers = []
    with open(file) as f:
        for line in f:
            numbers.append(line.strip())
    return numbers




def list_of_route_cost(number_file, route_cost_csv):

    numbers = get_numbers_list(number_file)
    prices =  []
    for number in numbers:
        cost = route_cost_check(number, route_cost_csv)
        if cost is not None:
            prices.append(cost)

    return prices


# print(get_numbers_list('phone-numbers-10.txt'))
print(list_of_route_cost('phone-numbers-100.txt', 'route-costs-35000.txt'))