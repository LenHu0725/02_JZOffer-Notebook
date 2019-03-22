# -*- coding: utf-8 -*-
"""
名称:   从尾到头打印链表每个节点的值
题目:   输入一个链表，从尾到头打印链表每个节点的值。
测试:   一个节点链表 多个节点链表 链表头结点为Nullptr 
"""

class Node(object):
    def __init__(self, value):
        self.val = value
        self.next = None


class Solution:
    def printListConvert(self, listNode):
        """
        输入链表 从尾到头打印链表每个节点的值
        输入：
        - listNode: 输入链表
        输出：
        - res: 输出打印
        """
        if not listNode:
            return []
        
        res = []
        while listNode.next is not None:
            res.append(listNode.val)
            listNode = listNode.next
        res.append(listNode.val)

        return res[::-1]


def main():
    import numpy as np

    data = np.random.randint(1, 100, 20)
    head = Node(data[0])

    p = head
    for i in data[1:]:
        node = Node(i)
        p.next = node
        p = p.next

    res = Solution.printListConvert(None, head)
    print("Origin data is :", data)
    print("Conver data is ：", res)



if __name__ == "__main__":
    main()

