# -*- coding：utf-8 -*-
"""
名称：  二叉树的下一个节点 【这道题考察二叉树遍历算法的理解】
题目：  给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
        【注意：树中的结点不仅包含左右子结点，同时包含指向父结点的指针】
测试：  普通二叉树（完全二叉树 不完全二叉树）
        特殊二叉树（所有节点都没有右子节点的二叉树；所有节点都没有左子节点的二叉树；只有一个节点的二叉树；二叉树的根结点指针为nullptr）
        不同位置的节点的下一个节点（下一个节点为当前节点的右子节点、右子树的最左子节点、父节点、跨层的父节点等；当前节点没有下一个节点）
"""

# 解题思路：见程序注释

class treeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution():
    def GoNext(self, pNode):
        """
        找到下一个节点
        输入：
        - pNode：已知节点
        输出：
        - pNode.next:   下一个节点
        """
        if not pNode:
            # S1: 异常处理
            return None

        elif not pNode.right:
            # S2: 该节点有右节点 右节点的左节点是下一节点
            pNode = pNode.right
            while pNode.left!=None:
                pNode = pNode.left
            return pNode
        elif pNode.next!=None and pNode.next.right==pNode:
            # S3:  无右节点 -> 该节点是父节点的右节点
            while pNode.next!=None and pNode.next.left!=pNode:
                pNode=pNode.next
            return pNode.next
        else :
            # S4: 无父节点
            return pNode
        
