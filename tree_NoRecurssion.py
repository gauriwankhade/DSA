
class node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None


class tree:
	def __init__(self):
		self.root = None
		self.stack = []
		self.visited = {}

	def add_node(self):
		self.root = node(1)
		root = self.root

		root.left = node(2)
		root.right = node(3)
		root.left.left = node(4)
		root.left.right = node(8)
		root.right.left = node(11)
		root.right.right = node(12)
		root.left.right.right = node(7)
		root.left.right.right.left = node(0)
		root.left.right.right.right= node(6)

		
	def post_order(self):
		node = self.root
		self.stack.append(node)
		self.visited[node] = True	# initial case

		while self.stack:
			if self.visited.get(node)== None:
				self.visited[node] = True
				self.stack.append(node)
			# if left node exists and not visited, Go left
			if node.left and (not self.visited.get(node.left)) :
				node = node.left
			# if right node exists and not visited, Go right
			elif node.right and (not self.visited.get(node.right)) : 
				node = node.right
			# if left node and right does not exists
			else:
				print node.value
				self.stack.pop()

				if self.stack:
					node = self.stack[-1]		# Backtrack
				else:
					break						# end case 

t = tree()
t.add_node()
t.post_order()




		
		
	
		
