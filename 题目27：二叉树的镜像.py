# -*- coding:utf-8 -*-
"""
名称：二叉树的镜像
题目：操作给定的二叉树 将其变为源的二叉树镜像
测试：
"""

# 解题方法：依次交换二叉树左右节点

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left  = None
        self.right = None


class Solution:
    def Mirror(self, tree):
        # 异常处理 根节点为空 返回None
        if not tree:
            return None

        # 无左右子树 返回空
        if not tree.left and tree.right:
            return None

        # 交换左右子树
        tmp = tree.left
        tree.left = tree.right
        tree.right = tmp

        # 递归左右子树
        if tree.left:
            self.Mirror(tree.left)

        if tree.right:
            self.Mirror(tree.right)