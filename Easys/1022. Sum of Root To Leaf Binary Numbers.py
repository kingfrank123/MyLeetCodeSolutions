# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # working with decimal representation
        # looking at the problem i have to visit all the nodes at least once(bottom leafs)
        # i think i will go with a linear time complexity and work from there
        count = 0
        # my stack will keep track of both node and its value
        stack = [(root,0)]
        while stack:
            node, curr_num = stack.pop()
            if node: # if node is not Null keep going
                # left shifting by 1 and bitwise with val (0 or 1)
                # left shifting by 1 will double curr_num 
                # since node.val (0 or 1) the only result after bitwise is +1 or remains same
                curr_num = (curr_num << 1) | node.val
                # if leaf(meaning both left and right leaf are Null), update sum
                if not node.left and not node.right:
                    count += curr_num
                else:
                    stack.append((node.right,curr_num))
                    stack.append((node.left,curr_num))
        return count
        # T(n) n = # of nodes
        # S(h) h = tree height (essentially max stack size)
