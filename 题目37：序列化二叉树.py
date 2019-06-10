# -*- coding:utf-8 -*-
"""
名称：序列化二叉树
题目：请实现两个函数，分别用来序列化和反序列化二叉树；
测试：功能测试：输入二叉树是完全二叉树；
     所有节点都没有左/右子树的二叉树；
     只有一个节点的二叉树；所有节点的值都有相同的二叉树；
     特殊测试：指向二叉树根节点的指针为nullptr指针；
"""

# 解题思路：

class nodeTree:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left  = None


class Solution:
    flag = -1
    
    def Serialize(self, root):
        if not root:
            return '#'

        return str(root.val) + ',' + self.Serialize(root.left) 
               + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        self.flag += 1
        lis = s.split(',')

        if self.flag >= len(s):
            return None

        root = None
        if lis[self.flag] != '#':
            root TreeNode(int(lis[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)

        return root