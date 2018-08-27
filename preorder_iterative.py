def preorder_iterative(root):
    if not root:
        return []

    values = []
    node_stack = [root]

    while len(node_stack) > 0:
        node = node_stack.pop()
        values.append(node.val)
        if node.right:
            node_stack.append(node.right)
        if node.left:
            node_stack.append(node.left)

    return values
