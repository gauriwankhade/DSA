class node: 
	"""docstring for Node"""
	def __init__(self,value):
		
		self.value = value
		self.left = None
		self.right = None
		

class bs_tree:
	"""docstring for bs_tree"""
	def __init__(self):
	
		self.root = None
		self.maxx = -999999
		self.loc = 0



	def insert_bs(self,item):
		# self.length+=1
		if self.root==None:
			self.root=node(item)


		else:
			self.root=self.insert_bs2(self.root,item)

	def insert_bs2(self,curr,item): 
		
		if curr.value>item:
			if curr.left==None:
				curr.left = node(item)
			else:
				curr.left=self.insert_bs2(curr.left,item)
		else:
			if curr.right==None:
				curr.right = node(item)
			else:
				curr.right=self.insert_bs2(curr.right,item) 
		return curr


	def print_bst(self):
		if self.root!=None:
			# return
			self.print_bst2(self.root)

	def print_bst2(self,curr):
		
		if curr!=None:
			# return 
			#print curr.value

		# if curr.left!= None:
			self.print_bst2(curr.left)
			#print curr.value
			# elif curr.right!= None:
			self.print_bst2(curr.right)
			self.maxx=max(curr.value,self.maxx)
			print curr.value

			# return curr.left.value
			# else:
			# 	return



	# def maximum_(self):
	# 	print self.maxx

	
	def find_(self,item):
		if self.root==None:
			print 'item not found...tree is empty'
			return

		self.find_2(self.root,item)


	def find_2(self,current,item):

		if current!= None:
			if current.value==item:
				print 'item found '
				return
			if current.value>item:
				print 'go left'
				self.find_2(current.left,item)
			else:
				print 'go right'
				self.find_2(current.right,item)
		else:
			print 'item not found'



	def delete_node(self,item):
		
		if self.root==None:
			print 'cant delete....tree is empty!!'
			return
		self.root=self.delete_node2(self.root,item)


	def delete_node2(self,curr,item):
		
		if curr!= None:
			if curr.value==item:
				# print 'deleted %d'%item
				# curr = None
				# return None

				if curr.left:
					left=curr.left
					curr=None
					return left
				elif curr.right:
					right=curr.right
					curr=None
					return right
				else:
					curr=None
					return None

			
			if curr.value> item:	
				curr.left=self.delete_node2(curr.left,item)
				
			elif curr.value< item:
				curr.right=self.delete_node2(curr.right,item)
				

		return curr





n=input()
b=bs_tree()
for i in range(n):
	num=input()
	b.insert_bs(num)
b.delete_node(5)
b.print_bst()
#b.maximum_()
# b.find_(55)
















		







# https://codeforces.com/contest/1322/problem/E

		