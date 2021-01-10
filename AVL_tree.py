class node:
	"""docstring for AVL"""
	def __init__(self,value):
		
		self.value = value
		self.height = 1
		self.left = None
		self.right = None

class AVL_tree:
	"""docstring for AVL_tree"""        
	def __init__(self):		
		self.root = None

	def insert(self,item):
		if self.root==None:
			self.root=node(item)
			return
		self.root=self.insert2(self.root,item)

		# if self.root==None:
		# 	self.root=node(item)
		# else:
		# 	self.root = self.insert2(self.root,item)

	def insert2(self,curr,item):
		
		if curr.value>item:
			if curr.left==None:
				curr.left=node(item)
			else:
				self.left=self.insert2(curr.left,item)

		else:
			if curr.right==None:
				curr.right=node(item)
			else:
				self.right=self.insert2(curr.right,item)
	 	

	# def insert2(self,curr,item):
	# 	if curr is None:
	# 		return node(item)
	# 	elif item < curr.value:
	# 		curr.left = self.insert2(curr.left,item)
	# 	else:
	# 		curr.right = self.insert2(curr.right,item)

		curr.height=1+max(self.get_height(curr.left),self.get_height(curr.right))
		balanceFactor= self.get_height(curr.left)-self.get_height(curr.right)

		if balanceFactor>1 and curr.left.value>item :
			return self.right_rot(curr)
	
		if balanceFactor< -1 and curr.right.value<item:
			return self.left_rot(curr)

		if balanceFactor>1 and curr.left.value<item:
			curr.left = self.left_rot(curr.left)
			return self.right_rot(curr)

		if balanceFactor<-1 and curr.right.value>item:
			curr.right = self.right_rot(curr.right)
			return self.left_rot(curr)
			
		return curr 
		
		

	def get_height(self,curr):
		if curr==None:
			return 0
		return curr.height
		


	
	def right_rot(self, root):
		# root.height= 1+max(self.get_height(root.left),self.get_height(root.right))
		# root.left = 1+max(self.get_height(root.left.left),self.get_height(root.left.right))

		
		w=root.left
		root.left=w.right
		w.right=root
		
		w.right.height = 1+max(self.get_height(w.right.left),self.get_height(w.right.right))
		w.height= 1+max(self.get_height(w.left),self.get_height(w.right))
		
	
		return w


	def left_rot(self, root):
		# root.height = 1+max(self.get_height(root.left),self.get_height(root.right))
		# root.right.height = 1+max(self.get_height(root.right.left),self.get_height(root.right.right)) 


		w=root.right
		root.right=w.left
		w.left=root

		w.left.height= 1+max(self.get_height(w.left.left),self.get_height(w.left.right))
		w.height= 1+max(self.get_height(w.left),self.get_height(w.right))


		
		
		return w


	def LR_rot(self, root):
		
		self.left_rot(root.left)
		self.right_rot(root)

	def RL_rot(self, root):
		self.right_rot(root.right)
		self.left_rot(root)


	def print_tree2(self):
		if self.root==None:
			return
		self.print_tree(self.root)


	def print_tree(self,root):
		if root==None:
			return
		# print root.value
		print root.value,'value'
		print root.height,'height'
		self.print_tree(root.left)
		
		
		self.print_tree(root.right)



avltree = AVL_tree()
# avltree.insert(1)
# avltree.insert(2)
# avltree.print_tree2()
# avltree.left_rot()
# avltree.print_tree2()
n=input()
for i in range(n):
	num= input()
	avltree.insert(num)

avltree.print_tree2()
		


		












		








		