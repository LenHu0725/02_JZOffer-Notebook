# -*- coding: utf-8 -*-
"""
名称：复杂链表的复制
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
     返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
测试：
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next  = None
        self.random = None


# 解题思路1：python内置函数法
class Solution1:
    def Clone(self, pHead):
        import copy
        return copy.deepcopy(pHead)



# 解题思路2: 分解法
class Solution2:
    def clone(self, pHead):
        """
        复制特殊链表
        输入：
        - pHead：链表头
        """
        if pHead==None:
            return None
        self.cloneNode(pHead)
        self.connectRandomNode(pHead)
        return self.ReconectRandomNode(pHead)
        

    def cloneNode(self, pHead):
        """
        将链表N后加入N'
        输入：
        - pHead：头节点
        """
        pNode = pHead
        while pNode:
            cloneNode = RandomListNode(pNode.label)
            cloneNode.next = pNode.next
            
            pNode.next = cloneNode
            pNode = cloneNode.next


    def connectRandomNode(self, pHead):
        """
        连接Random
        """
        pNode = pHead
        while pNode:
            pClone = pNode.next
            if pNode.random!=None:
                pClone.random = pNode.random.next
            pNode = pClone.next


    def ReconectRandomNode(self, pHead):
        """
        拆分链表
        """
        pNode = pHead
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next
        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode=pNode.next
        return pCloneNode



# 解题思路3: 递归法
class Solution3:
    def clone(self, pHead):
        if pHead == None:
            return None

        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next   = self.clone(pHead.next)

        return newNode 
