# -*- coding:utf-8 -*-
"""
名称：合并两个排序的链表
题目：输入两个单调递增的链表，输出两个链表合成后的链表，合成后的链表满足单调不减规则。
测试：功能测试：输入两个链表有多个节点 节点的值不相同或者存在值相等的多个节点；
     特殊测试：两个链表一个或两个头节点为null指针，两个链表中只有一个节点；
"""

# 解题思路：递归，注意对空链表单独处理；
class ListNode:
    def __init__(self, x):
        self.val  = x
        self.next = None


class Solution:
    def Merge(self, pHead1, pHead2):
        """
        合并两个链表
        输入：
        - pHead1:输入链表
        - pHead2:输出链表
        输出：
        - pHead:合并链表
        """
        # 异常处理 链表1&链表2 都为空
        if not pHead1:
            if not pHead2:
                print("P1 & P2 is None!")
                return None
            else:
                return pHead2
        elif not pHead2:
            return pHead1

        # 合并链表
        pMergeHead = None
        if (pHead1.val<pHead2.val):
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)

        return pMergeHead