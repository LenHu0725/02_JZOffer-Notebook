# -*- coding:utf-8 -*-
"""
名称：数组中出现次数超过一半的数字
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
     例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
     由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2，如果不存在则输出0。
测试：功能测试：输入数组中存在一个出现次数超过数组长度一半的数字；
             输入的数组中不存在一个出现次数超过数组长度一半的数字；
     边界测试：输入的数组中只有一个数字，输入nullptr指针；

"""

# 思路1: 键值对
class Solution_1:
    def MoreThanHalfNumSolution(self, numbers):
        """
        键值对 用字典实现
        """
        dict = {}
        for num in numbers:
            dict[num] = 1 if num not in dict else dict[num]+1
            if dict[num] > len(numbers)/2:
                return num
        return 0


# 思路2: 遍历元素 记录次数 若与前一个相同则加1 否则次数减1
class Solution_2:
    def MoreThanHalfNumSolution(self, numbers):
        # S0: 异常处理
        lenNums = len(numbers)
        if lenNums == 0:
            return 0
        
        # S1: 遍历元素 统计出现次数
        res = numbers[0]
        count = 1

        for i in range(1, lenNums):
            if count == 0:
                res = numbers[i]
                count = 1
            elif numbers[i] == res:
                count += 1
            elif numbers[i] != res:
                count -= 1

        # S2: 判断res是否符合条件 出现次数大雨数组长度一半
        counts = 0
        for j in range(lenNums):
            if numbers[j] == res:
                counts += 1
        
        if counts > lenNums//2:
            return res
        else:
            return 0

