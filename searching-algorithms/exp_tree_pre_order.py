class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


class ExpressionTree:
    def __init__(self):
        self.root = None

    def pre_order(self, current_node):
        # Check if current_node exists
        if current_node:
            # Print the value of the current_node
            print(current_node.data)
            # Call pre_order recursively on the appropriate half of the tree
            self.pre_order(current_node.left_child)
            self.pre_order(current_node.right_child)


if __name__ == "__main__":
    et = ExpressionTree()
    et.root = TreeNode("*")
    et.root.left_child = TreeNode("-")
    et.root.right_child = TreeNode(3)
    et.root.left_child.left_child = TreeNode(10)
    et.root.left_child.right_child = TreeNode(5)
    et.pre_order(et.root)
