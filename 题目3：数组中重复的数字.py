# -*- coding: utf-8 -*-
"""
名称： 数组中重复的数组
题目： 长为n的数组（数字为0-n-1），某些数字是重复的，不知道有几个重复，也不知道重复几次。
       请找出任意一个重复的数字。
       Eg. {2， 3， 1， 0， 2， 5， 3，} 重复的是2或3
"""


class Solution_1:
    """
    先把输入数组排序 再从排序后的数组中从前往后找
    
    输入：
    - numbers：输入数组

    输出：
    - duplication： 存在重复: 输出重复数字；
                    任何输入错误输出: -1；
                    不存在重复数字则输出: -2；
    """
    def __init__(self, numbers):
        self.numbers = numbers

    def duplicate(self, numbers):
        # S1:异常处理 [空值 小于0 超过范围数字]
        if numbers == None or len(numbers)<1:
            return -1

        for i in range(len(numbers)):
            if numbers[i]<0 or numbers[i]>len(numbers)-1:
                return -1

        # S2:排序 numbers.sort() 下使用冒泡排序法代替
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                if numbers[i]<numbers[j]:
                    numbers[j], numbers[i] = numbers[i], numbers[j]
        
        # S3:重复检测
        for i in range(len(numbers)-1):
            if numbers[i]==numbers[i+1]:
                return numbers[i]

        return -2
