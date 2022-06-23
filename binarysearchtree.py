
class Treenode:

    def __init__(self, key, val, left=None, right=None, parent=None) -> None:
        self.key = key
        self.value = val
        self.left_child: Treenode = left
        self.right_child: Treenode = right
        self.parent: Treenode = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child and self.right_child)

    def has_any_child(self):
        return self.left_child or self.right_child

    def has_both_child(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.value = val
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_child():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for item in self.left_child:
                    yield item
            yield self.key
            if self.has_right_child():
                for item in self.right_child:
                    yield item


class Binarysearchtree:

    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def lenth(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                self.left_child = Treenode(key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                self.right_child = Treenode(key, value, parent=current_node)

    def put(self, k, v):
        if self.root:
            self._put(k, v, self.root)
        else:
            self.root = Treenode(k, v)
        self.size += 1

    def __setitem__(self, k, v):
        self.put(k, v)

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.key
            else:
                return None
        else:
            return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self.get(key):
            return True
        return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, current_node: Treenode):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_child():
            min_child = current_node.right_child.find_min()
            if current_node.is_right_child():
                min_child.left_child = current_node.left_child
                current_node.parent.right_child = current_node.right_child
            elif current_node.is_left_child():
                min_child.left_child = current_node.left_child
                current_node.parent.left_child = current_node.right_child
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key, current_node.left_child.value,
                                                   current_node.left_child.left_child, current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.value, current_node.right_child.left_child, current_node.right_child.right_child)


if __name__ == "__main__":
    bst = Binarysearchtree()
    bst[70] = 'tom'
    bst[93] = 'bob'
    bst[15] = 'sam'
