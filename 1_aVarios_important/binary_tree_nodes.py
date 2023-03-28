# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
"""For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar."""

"""Example7
root1 = [3,5,1,6,2,9,8,null,null,7,4], 
root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
       3			 3
     /   \		   /   \
    5     1		  5     1
   / \   /  \	 / \   / \
  6   2 9   8	6   7 4   2
     / \		         / \
    7   4		        9   8
leaf root1 = [6,7,4,9,8]
leaf root2 = [6,7,4,9,8]
output = True		 
"""
# definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Convert the list to a binary tree
def buildTree(lst):
    def helper(nodeIndex):
        if nodeIndex >= len(lst) or lst[nodeIndex] is None:
            return None
        node = TreeNode(lst[nodeIndex])
        node.left = helper(nodeIndex * 2 + 1)
        node.right = helper(nodeIndex * 2 + 2)
        return node
    return helper(0)

# create the solution class, check that their leafs are equals
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))
    
root1 = buildTree([3,5,1,6,2,9,8,None,None,7,4,])
root2 = buildTree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])

leaf = Solution()
print(leaf.leafSimilar(root1, root2))


