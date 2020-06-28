class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, value):
        self.root_node = Node(value)
        self.size = 1

    def size(self):
        print(self.size)

    def insert(self, value):
        self.size += 1
        new_node = Node(value)

        def traverse(node):
            if value < node.value:
                if not node.left:
                    node.left = new_node
                else:
                    traverse(node.left)

            if value >= node.value:
                if not node.right:
                    node.right = new_node
                else:
                    traverse(node.right)

        traverse(self.root_node)

    def contain(self, value):
        cur = self.root_node
        while cur:
            if value == cur.value:
                print(f'contains: {value}')
                return True

            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
            print(f'contains: {value}')
            return False
