class Node:
	def __init__(self, value = None):
		self.left = None
		self.right = None
		self.data = value

	def __print(self):
		if self.left is not None:
			self.left.__print()
		print(self.data, end = ' ')
		if self.right is not None:
			self.right.__print()

class Tree:
	def __init__(self):
		self.root = None

	def print(self):
		if self.root is not None:
			self.root._Node__print()
		print()

	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
			return
		tmp = self.root
		while (1):
			if value < tmp.data:
				if tmp.left is None:
					tmp.left = Node(value)
					return
				tmp = tmp.left
				continue
			if tmp.right is None:
				tmp.right = Node(value)
				return
			tmp = tmp.right
			continue
