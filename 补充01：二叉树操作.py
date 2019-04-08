# -*- coding:utf-8 -*-
"""
名称：  二叉树操作
作者：  Hoo
日期：  2019.04.08
说明：  - 参考资料1: https://blog.csdn.net/xskxushaokai/article/details/78804685
       - 参考资料2: https://blog.csdn.net/wenkenza5368/article/details/79573333
"""

#1: 构建二叉树
class BTree:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        self.parent = None
    def insetleft(self, val):
        self.left = BTree(val)
        self.left.parent = self
        return self.left
    def insetright(self, val):
        self.right = BTree(val)
        self.right.parent = self
        return self.right
    def show(self):
        print(self.data)


#2: 三种遍历方式 - 前序遍历 中序遍历 后序遍历
def preorder(node):
    """ 前序遍历 """
    if node.data:
        node.show()
        if node.left:
            preorder(node.left)
        if node.right:
            preorder(node.right)

def inorder(node):
    """ 中序遍历 """
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)

def postorder(node):
    """ 后序遍历 """
    if node.data:
        if node.right:
            postorder(node.right)
        if node.left:
            postorder(node.left)
        node.show()


#3: 操作
def insert(node, value):
    """ 插入 """
    pass

def search(node, k):
    """ 查询 """
    pass
