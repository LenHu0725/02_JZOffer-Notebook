# -*- coding:utf-8 -*-
"""
名称：树的子结构
题目：输入两棵二叉树A和B，判断B是不是A的子结构；
测试：
"""

# 解题思路：

class TreeNode:
    def __init__(self, x):
        self.val   = x
        self.left  = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        """
        查找子树结构
        输入：
        - pRoot1:
        - pRoot2:
        输出：
        - res:
        """
        res = False    # 定义res为


        if pRoot1 and pRoot2:
            if proot1.val == pRoot2.val:
                res = SubtreeCore(pRoot1, pRoot2)
            
            if not res:



    def SubtreeCore(self, pRoot1, pRoot2):
        """
        
        """