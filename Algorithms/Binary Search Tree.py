class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # represents a way to connect left branch
        self.right = None  # represents a way to connect right branch


class BST:
    # let BST --> binary search tree

    def __init__(self, value=None):
        if value is not None:
            self.root = Node(value)
            self.size = 1
        else:
            self.root = None
            self.size = 0

        # self.size = 0 # increase after insertion / decrease after deletion

    # Recursive insert solution
    def __inserter(self, target, current_node):
        if current_node is None:
            current_node = Node(target)
            return True
        elif target == current_node.value:
            return False
        else:
            if target < current_node.value:
                # we must also check ... is the current_node's left empty
                if current_node.left is None:
                    current_node.left = Node(target)
                    return True
                else:
                    return self.__inserter(target, current_node.left)
            else:
                # we must check either right side is empty or we traversal the right side
                if current_node.right is None:
                    current_node.right = Node(target)
                    return True
                else:
                    return self.__inserter(target, current_node.right)

    def insert(self, target):
        # don't allow duplicates
        if self.root is None:
            self.root = Node(target)
            self.size += 1
            return True
        else:
            result = self.__inserter(target, self.root)
            if result:
                self.size += 1

            return result

    def search(self, target):
        # return True if target exists or False if target does not exist
        # non-recursive
        current_node = self.root
        while current_node is not None:
            if current_node.value == target:
                return True
            elif target < current_node.value:
                # travel to the left subtree
                current_node = current_node.left
            else:
                current_node = current_node.right

        # if we run into an empty node, we return False
        return False

    def __lister(self, current_node, result=[]):
        if current_node is None:
            return []

        left_side = self.__lister(current_node.left)
        current = [current_node.value]
        right_side = self.__lister(current_node.right)

        return left_side + current + right_side

    def toList(self):
        # returns a sorted list from BST object
        return self.__lister(self.root)

    def minimum(self, node_obj):
        current_node = node_obj

        while current_node.left is not None:
            current_node = curent_node.left

        return current_node.value

    def maximum(self, node_obj):
        current_node = node_obj

        while current_node.right is not None:
            current_node = curent_node.right

        return current_node.value

    # can we update value?
    def update(self, target, replacement):
        # rule #1, replacement can't exists
        current_node = self.root
        if self.search(replacement):
            return False

        # rule #2, the target has to exist
        if self.search(target):
            # rule 2a, replacement must be less than all the values to the right of the target and must be greater than all the values to the left of the target
            traversal = True
            while traversal:
                if current_node is None:
                    return False
                elif current_node.value == target:
                    # we must check left and right

                    if current_node.left:
                        left_max = self.maximum(current_node.left)
                    if current_node.right:
                        right_min = self.minumum(current_node.right)
                    if left_max < replacement < right_min:
                        current_node.value = replacement
                        return True
                elif target < current_node.value:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
        else:
            return False

    def __delete_helper(self, target, node_obj):
        if node_obj.left and node_obj.right:
            sucessor = self.minimum(node_obj.right)
            self.delete(sucessor, node_obj.right)
            result = Node(sucessor)
            result.left = node_obj.left
            return

        elif node_obj.left:
            return node_obj.left
        elif node_obj.right:
            return node_obj.right
        else:
            return None

    def delete(self, target, node_obj=None):
        if self.root is None:
            return False
        else:
            if node_obj is None:
                current_node = self.root
            else:
                current_node = node_obj

                if target < current_node.value:
                    if target == current_node.left.value:
                        replacement = self.__delete_helper(current_node.left)
                        current_node.left = replacement
                        return True
                    else:
                        current_node = current_node.left

                elif target > current_node.right.value:
                    if target == current_node.right.value:
                        replacement = self.__delete_helper(current_node.right)
                        current_node.left = replacement
                    else:
                        current_node = current_node.right

            return False


data = BST()
data.insert(3)
data.insert(9)
data.insert(11)
data.insert(4)
data.insert(10)
data.insert(1)

print(data.search(5))
print(data.search(19))
data_list = data.toList()
print(data_list)