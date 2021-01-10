class node():
	"""docstring for Node"""
	def __init__(self,key):
		
		self.key = key
		self.left = None
		self.right = None

def trees():
	root= node(1)
	root.left = node(2)
	root.right = node(3) 
	root.left.left= node(4)
	root.left.right= node(5)
	root.right.left = node(6)
	root.right.right = node(7)
	return root


def print_tree(root):
	if root==None:
		return
	print root.key
	print_tree(root.left)
	
	print_tree(root.right)
	



root=trees()
print_tree(root)




		