from trie import PrefixTree
from helper import read_str_list
import pickle

def get_prefix_cost(phone_nums, trie):
	''' Given a list of phone numbers, return a list of costs '''

	price_output = []

	# loop through phone numbers
	for phone_num in phone_nums:
		# remove '+'
		phone_num = phone_num[1:]
		# get cost with search function in prefix tree class
		price = trie.search(phone_num)
		price_output.append(price)
	
	return price_output


def build_prefix_tree(file):
	''' Builds a prefix tree according to input data '''

	# init prefix tree
	prefix_tree = PrefixTree()

	# get prefix and cost from generator as list of tuples
	lines = read_str_list(file)

	for prefix, price in lines:
		prefix_tree.insert(prefix[1:], float(price))

	return prefix_tree

if __name__ == '__main__':
	# prefix_cost = 'route-costs-35000.txt'

	# prefix_tree = pickle.load(open('trie.pickle', 'rb'))

	# with open('data/results-3.txt', 'w') as out:
	# 	numbers = (number for number in open('data/phone-numbers-10000.txt').read().splitlines())
	# 	for number in numbers:
	# 		cost = prefix_tree.search(number)
	# 		out.write(f'{number},{cost}\n')

	prefix_tree = build_prefix_tree('route-costs-35000.txt')
	phone_nums = read_str_list('phone-numbers-10000.txt')
	print(get_prefix_cost(phone_nums, prefix_tree))