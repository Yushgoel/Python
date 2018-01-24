class Stack(object):
	"""docstring for Stack"""
	
	def __init__(self):
		self.last_index = 0
		self.my_stack = []

	def push(self, element):
		self.my_stack.append(element)
		self.last_index += 1
		print self.last_index

	def stack_pop(self):
		returner = self.my_stack[self.last_index-1]
		self.my_stack.pop(self.last_index-1)
		self.last_index -= 1
		print returner
		return returner;

Stack1 = Stack()
Stack1.push("plate1")
Stack1.push("plate2")
Stack1.push("plate3")

Stack1.stack_pop()