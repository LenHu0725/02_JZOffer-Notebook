# -*- coding: utf-8 -*-
"""
名称：包含min函数的栈
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
     在该栈中，调用min、push、pop的时间复杂度都是O(1)
测试：新压入栈的数字比之前的最小值大；
     新压入栈的数字比之前的最小值小；
     弹出栈的数字不是最小元素；
     弹出栈的数字是最小元素；
"""

# 解题思路：一个主栈 一个辅助栈，辅助栈用于保存当前最小值；

class Solution:
    def __init__(self):
        self.stack = []
        self.minstack=[]


    def push(self, x):
        """
        压入新数据
        Input:
        - x：压入数据
        """
        self.stack.append(x)

        if self.stack==[] or x<self.min():
            self.minstack.append(x)
        else:
            self.minstack.append(self.min())


    def pop(self):
        """
        弹出数据
        """
        if self.stack==[]:
            return None

        self.stack.pop()
        self.minstack.pop()


    def top(self):
        """
        最上头数据
        """
        return self.stack[-1]


    def min(self):
        """
        最小数据
        """
        return self.minstack[-1] 
