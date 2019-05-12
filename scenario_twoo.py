# from scenario_one import route_cost_check

# def make_list_of_list(file):
#     ''' Return a 2d list of prefixes and costs '''
#     list_of_lists = []
#     with open(file) as f:
#         for line in f:
#             _list = line.strip().split(",")
#             list_of_lists.append(_list)
#     return list_of_lists

# def sort(2d_array):
#     ''' Sorts a 2d list '''


# def binary_search(list_of_list, item: [str]) -> (int, None):
#     return binary_search_recursive(list_of_list, item)

# def binary_search_recursive(array: [str], item: [str], left=None, right=None) -> (int, None):
#     ''' '''
#     if left == right and left is not None:
#         # case: traverse binary search from any direction and item is not found
#         if left == len(array):
#             return None
#         # case: check if index is item
#         elif array[left] == item:
#             return left
#         # case: item not found
#         else:
#             return None

#     # case: binary search
#     if left == None and right == None:
#         left = 0
#         right = len(array) 
#     # set middle index
#     middle_index = (left + right) // 2
#     # checks with either side of middle_index
#     if array[middle_index] == item:
#         return middle_index
#     # case: check 0 <= x <= middle_index
#     elif array[middle_index] > item:
#         right = middle_index - 1 
#     # case: check middle_index <= x <= right
#     elif array[middle_index] < item:
#         left = middle_index + 1 
#     return binary_search_recursive(array, item, left, right)

# print(list_of_route_cost('phone-numbers-100.txt', 'route-costs-35000.txt'))

