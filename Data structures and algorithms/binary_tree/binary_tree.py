from node import Node

class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with that value already exist!')
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break

    def printInOrder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node.value)
        self._inorder_recursive(current_node.right)

    def find(self, value: int) -> Node:
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
        raise LookupError(f'Node {value} doesnt exist!!!')

    def find_parent(self, value: int) -> Node:
        if self.head and value == self.head.value:
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left and value == current_node.left.value) or\
                    (current_node.right and value == current_node.right.value):
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
        raise LookupError(f'Node {value} doesnt exist!!!')

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.left and to_delete.right:
            #2 children
            rightmost_node = self.find_rightmost(to_delete.left)
            rightmost_parent_node = self.find_parent(rightmost_node.value)
            if rightmost_parent_node != to_delete:
                if rightmost_node.left:
                    to_delete.value = rightmost_node.value
                    rightmost_parent_node.right = rightmost_node.left
                else:
                    to_delete.value = rightmost_node.value
                    rightmost_parent_node.right = None
            else:
                to_delete.value = rightmost_node.value
                to_delete.left = None

        elif to_delete.left or to_delete.right:
            #1 children
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.left or to_delete.right
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.left or to_delete.right
            else:
                self.head == to_delete.right or to_delete.left
        else:
            #no children
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = None
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None
            else:
                self.head = None