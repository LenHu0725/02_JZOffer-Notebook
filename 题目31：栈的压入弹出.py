# -*- coding : utf-8 -*-
"""
名称：栈的压入 弹出元素
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
     假设压入栈的所有数字均不相等。
     例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
测试：功能测试：输入数组有多个数字或一个数字；
             第二个数组是或不是第一个数组表示的压入序列对应的栈的弹出序列
     特殊测试：两个输入指针为Null；
"""

# 解题思路：利用辅助栈，演绎压入弹出过程；

class Solution:
    def isPopOrder(self, pushV, popV):
        """
        压入栈的顺序
        Input: 
        - pushV: 压入栈
        - popV: 弹出栈
        """
        stack = []
        while popV:
            
            # 堆入等于弹出顺位
            if pushV and pushV[0]==popV[0]:
                pushV.pop(0)
                popV.pop(0)

            # 若辅助栈的栈顶是弹出元素 应直接弹出
            elif stack and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)

            # 不断往辅助栈压入元素
            elif pushV:
                stack.append(pushV.pop(0))

            else:
                return False

        return True
    