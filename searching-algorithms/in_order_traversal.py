from bst import BinarySearchTree


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert("Little Women")
    bst.insert("Heidi")
    bst.insert("Oliver Twist")
    bst.insert("Dracula")
    bst.insert("Jane Eyre")
    bst.insert("Moby Dick")
    bst.insert("Vanity Fair")
    bst.in_order(bst.root)
