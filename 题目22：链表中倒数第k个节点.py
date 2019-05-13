# -*- coding:utf-8 -*-
"""
名称：链表中倒数第k个节点
题目：输入一个链表，输出该链表中倒数第k个结点。
测试：功能测试：第k个节点在链表的中间；第k个节点是链表的头节点；第k个节点是列表的尾节点；
     边缘测试：链表的头节点为nullptr指针；链表的节点总数少于k；k等于0；
"""
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解题思路：定义两个指针，第一个指针永远位于第二个指针前k个；
#          当第一个指针位于结尾时，第二个指针正好位于倒数第k个位置；
# 异常处理：输入非链表，链表长度小于k
class Solution:
    def FindKthToTail(self, head, k):
        """
        找到序列中倒数第k个指针的位置
        输入：
        - head: 指针头
        - k: 寻找的第k个位置
        输出：
        - kIndex：第k个位置的指针
        """
        # 异常处理  
        if not head or k<=0:
            return None

        # 定义两个指针
        pFirst  = head
        pSecond = None

        # 首位两指针依次后移 直到移动到末尾
        for i in range(k-1):
            # 未移动到队尾 报错处理 否则第一个指针向下移动
            if pFirst.next:
                pFirst = pFirst.next

            else:
                return None

        # 移动到队尾 输出第二个指针
        pSecond = head
        while pFirst.next:
            pFirst = pFirst.next
            pSecond = pSecond.next

        return pSecond

