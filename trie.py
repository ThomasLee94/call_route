
class PrefixNode:

    def __init__(self):
        ''' init node for Trie Tree with None elements in list'''
        self.children_list = [None]*10
        self.cost = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.children_list)

    def is_leaf(self)->bool:
        ''' Return True if this node is a leaf'''
        for node in self.children_list:
            return node is None

    def is_branch(self):
     ''' Return True if this node is a branch (one child or more)'''
     for node in self.children_list:
         return node is not None

     def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.cost)

class PrefixTree:

    def __init__(self):
        ''' init trie tree '''
        self.root = PrefixNode()

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.root)

    def insert(self, prefix: str, cost: str):
        ''' inserts items in trie tree '''
        node = self.root
        
        for num in prefix:
            num = int(num)
            # check if key exists
            if not node.children_list[num]:
                # if not, set new key-value pair
                node.children_list[num] = PrefixNode()
            # if yes, traverse through tree
            node = node.children_list[num]

        # check if node has cost
        if node.cost is not None:
            # check if its the cheapest cost
            if cost > node.cost:
                # if it is, we already have the cheapest cost
                return
        # set cost
        node.cost = cost

    def search(self, phone_number: str) -> str:

        ''' Search through prefix tree to find cheapest assoicated
        cost with phone number '''

        # ignore '+' in phone number
        if phone_number[0] == '+': 
            phone_number = phone_number[1:]

        node = self.root
        cost = 0

        # loop through digits in phone number
        for num in phone_number:
            num = int(num)
            # if number of node exists in correct index
            if node.children_list[num] is not None:
                # traverse through prefix tree with phone number as index
                node = node.children_list[num]
                # check if cost exists
                if node.cost is not None:
                    # update cost
                    cost = node.cost

        # returning the most up-to-date cost
        if node.cost is not None:
            return node.cost
        else:
             return cost


