# -*- encoding: utf-8 -*-
"""
@File    : leetcode.py
@Time    : 2020/2/21 11:54
@Author  : hksong
"""

'''
完全平方数：
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
'''
class Solution:
    def maxProduct(self, nums ) -> int:
        # dp_max[i]表示以nums[i]结尾的最大的子序列乘积
        # dp_min[i]表示以nums[i]结尾的最小的子序列乘积
        # ans = max(dp_pos)
        dp_max = [False] * len(nums)
        dp_min = [False] * len(nums)
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp_max[i] = dp_min[i] = 0
            elif nums[i] > 0:
                dp_max[i] = max(dp_max[i-1]*nums[i], nums[i])
                dp_min[i] = min(dp_min[i-1]*nums[i], nums[i])
            elif nums[i] < 0:
                dp_max[i] = max(dp_min[i-1]*nums[i], nums[i])
                dp_min[i] = min(dp_max[i-1]*nums[i], nums[i])
        return max(max(dp_min), max(dp_max))




'''
从前序和后序，恢复树
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def helper(preo, ino):
            if preo:
                root = TreeNode(preo[0])
                root_i = ino.index(preo[0])
                root.left = helper(preo[1:1+root_i], ino[:root_i])
                root.right = helper(preo[1+root_i:], ino[root_i+1:])
                return root
        return helper(preorder, inorder)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
slo = Solution()
node = slo.buildTree(preorder, inorder)

res=[]
def pre(node):
    if node:
        res.append(node.val)
        pre(node.left)
        pre(node.right)
    else:
        res.append("null")
pre(node)
print(res)