class Binarytree:

    def __init__(self, root_obj) -> None:
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = Binarytree(new_node)
        else:
            node = Binarytree(new_node)
            node.left_child = self.left_child
            self.left_child = node

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = Binarytree(new_node)
        else:
            node = Binarytree(new_node)
            node.right_child = self.right_child
            self.right_child = node

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, value):
        self.key = value

    def get_root_val(self):
        return self.key
