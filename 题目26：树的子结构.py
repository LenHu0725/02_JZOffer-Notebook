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
        - res: TRUE/FALSE
        """
        res = False    # 定义res为


        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.SubtreeCore(pRoot1, pRoot2)
            
            if not res:
                res = self.SubtreeCore(pRoot1.left, pRoot2)
            
            if not res:
                res = self.SubtreeCore(pRoot1.right, pRoot2)

        return res


    def SubtreeCore(self, pRoot1, pRoot2):
        """
        检查子树是否符合要求
        输入：
        - pRoot1:树
        - pRoot2:子树
        输出：
        - TRUE/FALSE
        """
        if pRoot1 == None:
            return None

        if pRoot2 == None:
            return None

        if pRoot1.val != pRoot2.val:
            return False

        return self.SubtreeCore(pRoot1.left, proot2.left) and 
               self.SubtreeCore(pRoot1.right, pRoot2.right)