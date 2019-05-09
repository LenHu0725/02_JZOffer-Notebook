# -*- coding:utf-8 -*-
"""
名称：调整数组的顺序使奇数位于偶数前面
"""

# 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序；
#      使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分；
# 测试：功能测试：输入数组中的奇数、偶数交替出现；
#              输入的数组中所有偶数都出现在奇数前面；
#              输入的数组中所有奇数都出现在偶数的前面；
#      特殊测试：输入nullptr指针 输入的数组只包含一个数字；
class Solution:
    def reOrderArray(self, array):
        """
        重新排序 
        判断数字在数组前半部分和后半部分的可能性
        输入：
        - array：输入序列
        输出：
        - array：输出
        """
        # 异常处理
        if array==None or len(array)==0:
            return None

        # 定义前后指针
        pBegin = 0
        pEnd   = len(array)-1

        while(pBegin<pEnd):
            # 前指针向后移动
            while pBegin<pEnd and not self.isEven(array[pBegin]):
                pBegin += 1

            # 后指针向前移动
            while pBegin<pEnd and self.isEven(array[pEnd]):
                pEnd   -= 1

            # 交换数据
            if pBegin<pEnd:
                temp = array[pBegin]
                array[pBegin] = array[pEnd]
                array[pEnd] = temp

        # 返回数组
        return array


    def isEven(self, number):
        """
        判断奇数 
        功能判断函数 提升程序的扩展性
        输入：
        - number：输入数字
        输出：
        - True/False 是否是奇偶数
        """
        return number & 1 ==0


# 变换：奇数和偶数保持相对位置不变
class Solution2:
    def reOrderArray(self, array):
        """
        创建两个列表 分别填入内容
        输入：
        - array：输入列表
        输出：
        - array：输出列表
        """
        # 异常处理
        if array==None or len(array)==0:
            return None

        # 创建两个数组 将数据填入
        res1 = []
        res2 = []

        for i in array:
            if self.isEven(i):
                res1.append(i)
            else:
                res2.append(i)

        return res1+res2


    def isEven(self, number):
        return number & 1 == 0
