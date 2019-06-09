# Demo of inorder, preorder, and postorder tree traverals.

class BinaryTreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def print_preorder(root):
	if root:
		print(root.val, end=" ")
		print_preorder(root.left)
		print_preorder(root.right)


def print_inorder(root):
	if root:
		print_inorder(root.left)
		print(root.val, end=" ")
		print_inorder(root.right)


def print_postorder(root):
	if root:
		print_postorder(root.left)
		print_postorder(root.right)
		print(root.val, end=" ")


def main():
	root = BinaryTreeNode(10)
	root.left = BinaryTreeNode(20)
	root.right = BinaryTreeNode(30)
	root.left.left = BinaryTreeNode(40)
	root.left.right = BinaryTreeNode(50)

	print("Binary tree in-order traversal:")
	print_inorder(root)
	print("")

	print("Binary tree pre-order traversal:")
	print_preorder(root)
	print("")

	print("Binary tree post-order traversal:")
	print_postorder(root)
	print("")


if __name__=="__main__":
	main()
