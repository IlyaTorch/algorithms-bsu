class Node:
    def __init__(self, insert_value):
        self.left = None
        self.right = None
        self.value = insert_value
        self.left_count = 0

    def do_left_rotation(self):
        right_child = self.right
        temp = right_child.left
        right_child.left = self
        self.right = temp

    def do_right_rotation(self):
        left_child = self.left

        temp = left_child.right
        left_child.right = self
        self.left = temp

    def __str__(self):
        return f'value={self.value}, left_count={self.left_count}'


def insert_value_to_tree(root: Node, insert_value) -> Node:
    if root is None:
        return Node(insert_value)
    else:
        if insert_value > root.value:
            root.right = insert_value_to_tree(root.right, insert_value)
        else:
            root.left = insert_value_to_tree(root.left, insert_value)
            root.left_count += 1
    return root


def build_tree(*args) -> Node:
    root = Node(args[0])
    for item in args[1:]:
        root = insert_value_to_tree(root, item)
    return root


def walk_tree_increase(root: Node):
    if root:
        walk_tree_increase(root.left)
        print(root.value)
        walk_tree_increase(root.right)


def walk_tree_decrease(root: Node):
    if root:
        walk_tree_decrease(root.right)
        print(root.value)
        walk_tree_decrease(root.left)


def find_kth_min(root: Node, k: int) -> Node:
    if root is None:
        return Node(None)
    count = root.left_count + 1
    if count == k:
        return root
    if count > k:
        return find_kth_min(root.left, k)
    return find_kth_min(root.right, k - count)


if __name__ == '__main__':
    root = build_tree(50, 30, 20, 40, 70, 60, 80)
    print(find_kth_min(root, 3).value)
    # print('============')
    # walk_tree_increase(root)
    # print('============')
    # walk_tree_decrease(root)
