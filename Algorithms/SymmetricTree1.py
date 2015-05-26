__author__ = 'myang'


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = [(root.left, root.right)]

        while stack:
           left, right = stack.pop()
           if left is None and right is None:
               continue
           if left is None or right is None:
               return False
           if left.val != right.val:
               return False
           stack.append((left.left, right.right))
           stack.append((left.right, right.left))
        return True

