class BSTMap:
	def __init__(self):
		self._root = None
		self._size = 0

	def add(self, key, value):
		node = self._bstSearch_single(self._root, key)
		if node is not None:
			node.value = value
			return False
		else:
			self._root = self._bstInsert(self._root, key, value)
			self._size += 1
			return True

	def _bstInsert(self, subtree, key, value):
		if subtree is None:
			subtree = _BSTMapNode(key, value)
		elif key < subtree.key:
			subtree.left = self._bstInsert(subtree.left, key, value)
		elif key > subtree.key:
			subtree.right = self._bstInsert(subtree.right, key, value)
		return subtree

	def valueOf(self, key):
		node = self._bstSearch_single(self._root, key)
		assert node is not None, "Invalid map key."
		return node.value

	#READ:
	#This is my original implementation that writes straight to a dict. It works recursively and adds to an original dict instead of creating new lists on every recursive call
	#However it is not what is directly asked for so I have modified the function to follow spec/recommendations
	# def valuesOf(self, min, max): #values within a range
	# 	dict = {}
	# 	self._bstSearch(self._root, min, max, dict)

	# 	assert not dict == {}, "Invalid map key."

	# 	return dict

	def valuesOf(self, min, max): # search for values within a range
		nodes_list = self._bstSearch(self._root, min, max)

		nodes_dict = {}
		for node in nodes_list: #write found nodes to a dictionary
			nodes_dict[node.key] = node.value

		return nodes_dict #an empty list being returned is okay
		
	#search for a single value in the tree
	def _bstSearch_single(self, subtree, target):
		if subtree is None:
			return None
		elif target < subtree.key:
			return self._bstSearch_single( subtree.left, target)
		elif target > subtree.key:
			return self._bstSearch_single(subtree.right, target)
		else:    
			return subtree

	#READ:
	#This is my original implementation that writes straight to a dict. It works recursively and adds to an original dict instead of creating new lists on every recursive call
	#However it is not what is directly asked for so I have modified the function to follow spec/recommendations

	# def _bstSearch(self, subtree, min, max, dict):
	# 	if subtree is None:
	# 		return None
	# 	elif min <= subtree.key <= max: #if value is within the range 
	# 		left = self._bstSearch(subtree.left, min, max, dict) #search the left tree for values within range
	# 		right = self._bstSearch(subtree.right, min, max, dict) #search the right tree
	# 		dict[subtree.key] = subtree.value #add value to the dict
			
	# 		if left != None: 
	# 			dict[left.key] = left.value #if the left tree has a valid value then add it to the dict
	# 		if right != None:
	# 			dict[right.key] = right.value #if the right subtree is valid add it to the dict
	# 	elif subtree.key > max:
	# 		return self._bstSearch(subtree.left, min, max, dict)
	# 	elif subtree.key < min:
	# 		return self._bstSearch(subtree.right, min, max, dict)

	def _bstSearch(self, subtree, min, max):
		nodeslist = []

		if subtree is None:
			return nodeslist
		elif min <= subtree.key <= max:  #add node / it's children to the list if it / they is / are valid (within the range)
			left = self._bstSearch(subtree.left, min, max) #search the left tree for values within range
			right = self._bstSearch(subtree.right, min, max) #search the right tree
			
			nodeslist.append(subtree)
			if left != None: 
				nodeslist += left #add all valid nodes found on the left to the list
			if right != None:
				nodeslist += right #add all valid nodes found on the left to the list

			return nodeslist
		elif subtree.key > max:
			return self._bstSearch(subtree.left, min, max)
		elif subtree.key < min:
			return self._bstSearch(subtree.right, min, max)

class _BSTMapNode :
	def __init__( self, key, value ):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
	def __str__(self):
		return self.value

