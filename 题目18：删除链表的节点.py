# -*- coding: utf-8 -*-
"""
名称：删除链表中的节点
"""


# 题目：在O(1)时间内删除链表节点。
#      给定单向链表的头指针和一个节点指针，定义一个函数在O(1)时间内删除该节点。
# 测试：功能测试： 多个节点的链表的中间删除一个节点：
#               多个节点的链表中删除头节点；
#               多个节点的链表中删除尾节点；
#               一个节点的链表中删除唯一的节点；
#      特殊测试： 指向链表头节点的为nullptr指针；
#               指向要删除节点的为nullptr指针；

class ListNode:
    def __init__(self,):
        self.value = None
        self.next_node = None


class Solution:
    def delete_node(self, head_node, del_node):
        """ 
        删除某个节点
        输入：
        - head_node: 头节点
        - del_node: 删除节点
        """
        if not (head_node and del_node):
            return None

        # 删除的不是尾节点 将后面节点替换为当前节点
        if del_node.next_node:
            del_next_node = del_node.next_node
            del_node.value = del_next_node.value
            del_node.next_node = del_next_node.next_node

            del_next_node.value = None
            del_next_node.next_node = None

        # 只有一个头节点 
        elif del_node == head_node:
            head_node = None
            del_node = None

        # 多个节点删除尾节点
        else:
            node = head_node

            while node != del_node:
                node = node.next_node

            node.next_node = None
            node.value = None

        # 该方法无法处理不包含在列表内的节点
        return head_node
        

# 名称：删除链表中重复的节点
# 题目：在一个排序的链表中，请删除重复的节点，如1-2-3-3-4-4-5在重复的节点被删除后为1-2-5。
# 测试：功能测试：重复节点位于链表头部/尾部/中部；链表中没有重复的节点；
#      特殊测试：指向链表头节点的为nullptr指针；链表中所有节点都是重复的；

class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def deleteDulplication(self, pHead):
        """
        将链表元素保存在List中，过滤出现大于1的值，再重新形成链表
        输入：
        - pHead：链表头指针
        输出：
        - newList.next：重排后的头指针
        """
        res = []
        pNode = pHead

        while pNode.next:
            res.append(pNode.val)
            pNode = pNode.next

        res = list(filter(lambda c:res.count(c)==1), res)
        
        newList = listNode(0)
        pre = newList
        for i in len(res):
            node = listNode(i)
            pre.next = node
            pre = pre.next

        return newList.next



class Solution2:
    def deleteDulplication(self, pHead):
        """
        直接跳过重复列表节点
        输入：
        - pHead：链表头指针
        输出：
        - first.next：链表头指针
        """
        first = listNode(-1)
        first.next = pHead
        last = first


        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                
                while pHead and pHead.val==val:
                    pHead = pHead.next
                
                last.next = pHead

            else:
                last = pHead
                pHead = pHead.next


        return first.next
