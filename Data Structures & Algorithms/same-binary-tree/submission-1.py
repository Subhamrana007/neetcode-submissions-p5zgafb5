class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(root):
            res = []
            def traverse(node):
                if not node:
                    res.append(None)
                    return
                res.append(node.val)
                traverse(node.left)
                traverse(node.right)
            traverse(root)
            return res

        return inorder(p) == inorder(q)