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

	def valuesOf(self, min, max): #values within a range
		dict = {}
		self._bstSearch(self._root, min, max, dict)

		assert not dict == {}, "Invalid map key."

		return dict

	def _bstSearch_single(self, subtree, target):
		if subtree is None:
			return None
		elif target < subtree.key:
			return self._bstSearch_single( subtree.left, target)
		elif target > subtree.key:
			return self._bstSearch_single(subtree.right, target)
		else:    
			return subtree

	def _bstSearch(self, subtree, min, max, dict):
		if subtree is None:
			return None
		elif subtree.key <= max and subtree.key >= min:
			left = self._bstSearch(subtree.left, min, max, dict)
			right = self._bstSearch(subtree.right, min, max, dict)
			dict[subtree.key] = subtree.value
			
			if left != None:
				dict[left.key] = left.value
			if right != None:
				dict[right.key] = right.value
		elif subtree.key > max:
			return self._bstSearch(subtree.left, min, max, dict)
		elif subtree.key < min:
			return self._bstSearch(subtree.right, min, max, dict)

class _BSTMapNode :
	def __init__( self, key, value ):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
	def __str__(self):
		return self.value

