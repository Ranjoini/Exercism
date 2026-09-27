class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for item in tree_data[1:]:
            self._insert(self.root, item)

    def _insert(self, current_node, value):
        if value <= current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert(current_node.right, value)

    def data(self):
        return self.root

    def sorted_data(self):
        result = []

        def extract(node):
            if node is None:
                return
            extract(node.left)
            result.append(node.data)
            extract(node.right)

        extract(self.root)
        return result
