# -*- coding:utf-8 -*-
"""
名称：反转链表
题目：输入一个链表，反转链表并输出反转后链表的头节点
测试：功能测试：链表中有一个节点或多个节点；
     边界测试：链表头节点为nullptr指针
"""

# 解题思路：
# 用三个指针，依次从后一个指到前一个；

class Node:
    def __init__(self, x):
        self.val  = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        """
        反转链表
        输入：
        - pHead: 链表头指针
        输出：
        - pReverserHead: 链表反转后头指针
        """
        # 异常处理
        if pHead == None:
            return None

        # 异常处理并赋初始值
        pPrev = pHead

        if pHead.next == None :
            return pHead
        else:
            pNode = pHead.next

        if pNode.next == None:
            pNode.next = pHead
            pHead.next = None
            return pNode
        else:             
            pNext = pNode.next

        # 链表依顺序反转
        while pNext != None:
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
            
            pNext = pNext.next

        pNode.next = pPrev

        return pNode


