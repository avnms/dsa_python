class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = TreeNode(data)
        # Check if the BST is empty
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                # Check if the data is less than the current node's data
                if new_node.data < current_node.data:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                # Check if the data is greater than the current nodes' data
                elif new_node.data > current_node.data:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child

    def search(self, search_value):
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert("Pride and Prejudice")
    print(bst.search("Pride and Prejudice"))
