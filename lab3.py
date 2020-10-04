class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.left_count = None

    def __str__(self):
        if self.left and self.right:
            return f'value={self.value}, left={self.left.value}, right={self.right.value}'
        if self.left:
            return f'value={self.value}, left={self.left.value}, right=None'
        if self.right:
            return f'value={self.value}, left=None, right={self.right.value}'
        return f'value={self.value} left=None right=None'


class Tree(object):

    def insert(self, root: Node, value) -> Node:
        if root is None:
            return Node(value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        else:
            root.left = self.insert(root.left, value)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance_coefficient = self.get_balance_coefficient(root)

        # 4 cases for unbalanced nodes:

        # Case 1 - Left Left
        if balance_coefficient > 1 and value < root.left.value:

            return self.do_right_rotation(root)

        # Case 2 - Right Right
        if balance_coefficient < -1 and value > root.right.value:
            return self.do_left_rotation(root)

        # Case 3 - Left Right
        if balance_coefficient > 1 and value > root.left.value:
            root.left = self.do_left_rotation(root.left)
            return self.do_right_rotation(root)

        # Case 4 - Right Left
        if balance_coefficient < -1 and value < root.right.value:
            root.right = self.do_right_rotation(root.right)
            return self.do_left_rotation(root)

        return root

    def do_left_rotation(self, root: Node) -> Node:
        right_child = root.right
        left_of_right_child = right_child.left

        right_child.left = root
        root.right = left_of_right_child

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        right_child.height = 1 + max(self.get_height(right_child.left),
                           self.get_height(right_child.right))

        return right_child

    def do_right_rotation(self, root: Node) -> Node:
        left_child = root.left
        right_of_left_child = left_child.right

        left_child.right = root
        root.left = right_of_left_child

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        left_child.height = 1 + max(self.get_height(left_child.left),
                           self.get_height(left_child.right))

        return left_child

    def get_height(self, root) -> int:
        if not root:
            return 0
        return root.height

    def get_balance_coefficient(self, root) -> int:
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def draw_tree_order(self, root):
        if not root:
            return

        print(root)
        self.draw_tree_order(root.left)
        self.draw_tree_order(root.right)

    def walk_tree_increase(self, root: Node):
        if root:
            self.walk_tree_increase(root.left)
            print(root.value)
            self.walk_tree_increase(root.right)

    def walk_tree_decrease(self, root: Node):
        if root:
            self.walk_tree_decrease(root.right)
            print(root.value)
            self.walk_tree_decrease(root.left)


def find_kth_min(root: Node, k: int) -> Node:
    root.left_count = find_left_children_count(root)
    if root is None:
        return Node(None)
    count = root.left_count + 1
    if count == k:
        return root
    if count > k:
        return find_kth_min(root.left, k)
    return find_kth_min(root.right, k - count)


def build_tree(*values) -> (Tree, Node):
    root = None
    tree = Tree()
    for value in values:
        root = tree.insert(root, value)
    return tree, root


def find_total_nodes_count(root: Node):
    if not root:
        return 0
    if root.height == 1:
        return 1
    return 1 + find_total_nodes_count(root.left) + find_total_nodes_count(root.right)


def find_left_children_count(root: Node):
    if root.left:
        return find_total_nodes_count(root.left)
    return 0


if __name__ == '__main__':
    binary_tree, root = build_tree(4, 10, 15, 20, 23, 25, 29, 30, 37, 39, 40, 50, 44, 55)
    """ 
                       30 
                /               \ 
             20                  44 
        /          \        /          \ 
       10          25      39           50
      /  \        /  \    /  \           \
     4    15     23  29  37   40           55
    """
    # binary_tree.draw_tree_order(root)
    # binary_tree.walk_tree_increase(root)
    # binary_tree.walk_tree_decrease(root)
    print(find_kth_min(root, 5))
