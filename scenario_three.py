from trie import PrefixTree

def get_prefix_cost(phone_nums: [str], trie) -> [str]:
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

	