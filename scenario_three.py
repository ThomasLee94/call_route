from trie import PrefixTree
from helper import read_str_list
import pickle
from os.path import isfile

def build_prefix_tree(file_path):
	''' Builds a prefix tree according to input data '''
	# init prefix tree
	prefix_tree = PrefixTree()

	# get prefix and cost from generator as list of tuples
	lines = read_str_list(file_path)

	for prefix, price in lines:
		prefix_tree.insert(prefix[1:], float(price))

	return prefix_tree

def get_prefix_tree(n: int):
	""" n is the number of lines in desired cost-route-n.txt i.e n=35000 in route-costs-35000.txt """
	# checks if trie.pickle exists
	if isfile(f"route-costs-{n}.txt"):
		# load the pickle
		return pickle.load(open(f'trie-{n}.pickle', 'rb'))
	# if not, build prefix
	return  build_prefix_tree(f'route-costs-{n}.txt')

def find_cost(phone_nums):
	# search our pickled prefix tree
	prefix_tree = get_prefix_tree(35000)
	output_cost = list()

	for number in phone_nums:
		output_cost.append(prefix_tree.search(number))
	return output_cost

def compare_costs(correct_file, results_file):
	''' psuedo test function '''

	correct_costs = (l.split(",") for l in correct_file.read().splitlines())
	predicted_costs = (l.split(",") for l in results_file.read().splitlines())

	for truth, prediction in zip(correct_costs, predicted_costs):
		true_number, true_cost = truth
		_, predicted_cost = prediction

		if float(true_cost) < float(predicted_cost):
			print(true_cost, "is different from", predicted_cost, "for", true_number)


if __name__ == '__main__':
	# prefix_cost = 'route-costs-35000.txt'

	prefix_tree = pickle.load(open('trie-35000.pickle', 'rb'))

	# saving our prefix tree to disk by reading route costs and saving to results-x.txt
	# with open('results-35000.txt', 'w') as out:
	# 	number_costs = (line.split(",") for line in open('route-costs-35000.txt').read().splitlines())
	# 	for number, _ in number_costs:
	# 		print(number)
	# 		cost = prefix_tree.search(number)
	# 		out.write(f'{number},{cost}\n')

	#prefix_tree = build_prefix_tree('route-costs-35000.txt')
	#pickle.dump(prefix_tree, open("trie-35000.pickle", "wb"))

	# compare_costs(open('route-costs-35000.txt'), open('results-35000.txt'))
	phone_nums = (n[0] for n in read_str_list('phone-numbers-10000.txt'))
	print(find_cost(phone_nums))