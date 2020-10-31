class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # the main idea is to inorder traverse the BST
        # once prev.val > node.val is found, add the pair to swaps
        # if only one pair is found, then swap prev.val, node.val
        # if two pairs are found, swap the first prev.val with the second node.val
        prev, cur = TreeNode(float('-inf')), root
        stack, swaps = [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if prev.val > node.val:
                swaps.append([prev, node])
            prev, cur = node, node.right
        if len(swaps) == 1:
            swaps[0][0].val, swaps[0][1].val = swaps[0][1].val, swaps[0][0].val
        elif len(swaps) == 2:
            swaps[0][0].val, swaps[1][1].val = swaps[1][1].val, swaps[0][0].val