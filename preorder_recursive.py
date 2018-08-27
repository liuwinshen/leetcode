def preorder_traversal(root):
    if not root:
        return []
    values = []
    dfs(root, values)
    return values

def dfs(root, values):
    if root:
        values.append(root.val)
        dfs(root.left, values)
        dfs(root.right, values)
