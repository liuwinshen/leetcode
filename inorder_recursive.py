class Solution():
    def inorder_recursive(self, root):
        if not root:
            return []

        values = []
        self.dfs(root, values)
        return values

    def dfs(self, root, values):
        if root:
            self.dfs(root.left, values)
            values.append(root.val)
            self.dfs(root.right, values)
