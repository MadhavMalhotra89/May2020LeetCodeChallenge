# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def getAnswer(root, val):
            queue = collections.deque()
            queue.append((root, 0, None))
            found = False
            while queue:
                node, level, parent = queue.popleft()
                if node.val == val:
                    return ((level, parent))
                if node.left:
                    queue.append((node.left, level+1, node))
                if node.right:
                    queue.append((node.right, level+1, node))
            if not found:
                return (None, None)
        answer1 = getAnswer(root, x)
        answer2 = getAnswer(root, y)
        #print(answer1, answer2)
        if answer1[0] == answer2[0] and answer1[1].val != answer2[1].val:
            return True
        else:
            return False
