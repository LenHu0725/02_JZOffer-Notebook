# -*- coding: utf-8 -*-
"""
名称：链表中环的入口节点
题目：链表包含环，如何找出环的入口节点？
测试：功能测试：链表中包含环或不包含环；链表中有多个或者只有一个节点；
     边界测试：链表头节点为Null；
"""

# 解题：分解为三个问题
# Q1:  如何判断链表包含环？
# A1:  一次走两步的快指针 一次走一步的慢指针，若两指针会相遇表示存在环；
# Q2:  如何找到环的入口节点？
# A2:  列表=非环n个节点+环x个节点，上一问相遇时 p慢=x p快=2x=n+x n为一环数量；
#      将一个指针指向头，两个指针每次后指一个，相遇时指向的为入口；
# Q3:  如何得到环中节点数目？
# A3:  接第二问，此时仅移动一个指针，两指针再次相遇时，指针的移动数目为环的大小；

class Node:
    """ 链表中的点 """
    def __init__(self, x):
        self.val  = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead, isCircle):
        """  
        链表的入口节点
        输入：
        - pHead：链表头节点
        - isCircle：True/False 是否输出环中节点数
        输出：
        - pFast：链表环入口
        """
        # S0: 异常处理
        if pHead == None:
            return None

        # S1: 判断链表是否存在环
        pFast = pHead
        pSlow = pHead

        while pFast.next!=None and pFast!=None:
            pFast = pFast.next.next
            pSlow = pSlow.next

            if pFast == pSlow:
                break

        if pFast==None or pFast.next==None:
            return None

        # S2: 若存在环判断入口 重新让两指针相遇
        pSlow = pHead

        while pSlow!=pFast:
            pFast = pFast.next
            pSlow = pSlow.next

        # 是否输出节点数目
        if isCircle:
            return pFast
        else:
            numCircle = 0

            while pFast!=pSlow:
                pFast = pFast.next
                numCircle += 1

            return numCircle
