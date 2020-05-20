# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """self.arr = []
        self._inorder(root)
        return self.arr[k-1]
    def _inorder(self,root):
        if root == None:
            return
        self._inorder(root.left)
        self.arr.append(root.val)
        self._inorder(root.right)"""
        
        stack =  []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root =  stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
