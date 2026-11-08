# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root):
        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node)
            inorder(node.right)

        inorder(root)

        first = second = None

        for i in range(len(arr) - 1):
            if arr[i].val > arr[i + 1].val:
                if first is None:
                    first = arr[i]
                second = arr[i + 1]

        first.val, second.val = second.val, first.val

        