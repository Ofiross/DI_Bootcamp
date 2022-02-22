# Daily Challenge : Binary Search Tree

class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self, child_node):
        self.left = child_node

    def set_right(self, child_node):
        self.right = child_node

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def add_node(self, child_node):
        if self.value:
            if child_node < self.get_value():
                if self.left is None:
                    self.left = Node(child_node)
                else:
                    self.left.add_node(child_node)
            elif child_node > self.get_value():
                if self.right is None:
                    self.right = Node(child_node)
                else:
                    self.right.add_node(child_node)
        else:
            self.value = child_node

    def search_val(self, value):
        if value < self.get_value():
            if self.left is None:
                return str(value)+" Not Found"
            return self.get_left().search_val(value)

        elif value > self.get_value():
            if self.right is None:
                return str(value)+" Not Found"
            self.get_right().search(value)
        else:
            print(str(self.get_value()) + ' is found')

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value),
        if self.right:
            self.right.print_tree()


root = Node(12)
root.add_node(6)
root.add_node(14)
root.add_node(3)
root.search_val(6)
root.print_tree()
