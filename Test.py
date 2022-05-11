from BST import BST

test_tree = BST()

#working with an empty tree
print(test_tree.isEmpty())
print(test_tree.size())

#testing the put, get, and contain method
test_tree.put(1,'uno')
print(test_tree.get(1), test_tree.get(2))
print(test_tree.contains(1))

#testing max, min, and size
test_tree.put(2, 'dos')
test_tree.put(3, 'tres')
test_tree.put(0, 'cero')
test_tree.put(100, 'cien')

print(test_tree.size())
print(test_tree.max())
print(test_tree.min())