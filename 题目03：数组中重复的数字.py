# -*- coding: utf-8 -*-
"""
名称： 数组中重复的数组
题目： 长为n的数组（数字为0-n-1），某些数字是重复的，不知道有几个重复，也不知道重复几次。
       请找出任意一个重复的数字。
       Eg. {2， 3， 1， 0， 2， 5， 3，} 重复的是2或3
测试：  无效输入测试用例(输入空指针)；
        数组中不包含重复的数字；
        长度为n的数组里包含一个或多个重复的数字；
"""


class Solution_1:
    """
    先把输入数组排序 再从排序后的数组中从前往后找
    时间复杂度：O(n^2) 空间复杂度：O(1)
    输入：
    - numbers：输入数组

    输出：
    - duplication： 存在重复: 输出重复数字；
                    任何输入错误输出: -1；
                    不存在重复数字则输出: -2；
    """
    def __init__(self, numbers):
        self.numbers = numbers

    def duplicate(self):
        # S1:异常处理 [空值 小于0 超过范围数字]
        # if numbers == None or len(numbers)<1:
        if self.numbers.all() == None or len(self.numbers)<1:
            return -1

        for i in range(len(self.numbers)):
            if self.numbers[i]<0 or self.numbers[i]>len(self.numbers)-1:
                return -1

        # S2:排序 self.numbers.sort() 下使用冒泡排序法代替
        for i in range(len(self.numbers)):
            for j in range(i, len(self.numbers)):
                if self.numbers[i]<self.numbers[j]:
                    self.numbers[j], self.numbers[i] = self.numbers[i], self.numbers[j]
        
        # S3:重复检测
        for i in range(len(self.numbers)-1):
            if self.numbers[i]==self.numbers[i+1]:
                return self.numbers[i]

        return -2


class Solution_2:
    """
    使用辅助空间：哈希表 
    时间复杂度为：O[n] 空间复杂度为：O[n]
    输入：
    - numbers:  输入数组

    输出:
    - duplication:  存在重复数字: 输出重复数字
                    输入错误数字: 返回-1
                    不存在错误数字: 返回-2
    """
    def __init__(self, numbers):
        self.numbers = numbers

    def duplicate(self):
        # S1: 异常处理
        if self.numbers.all()==None or len(self.numbers)<1:
            return -1
        
        # S2: 处理多余值
        useDic = set(); duplication=-2
        for i in range(len(self.numbers)):
            # 异常值 [小于0 大于数组长度]
            if self.numbers[i]<0 or self.numbers[i]>len(self.numbers)-1:
                return -1
            
            # 判断重复
            if self.numbers[i] not in useDic:
                useDic.add(self.numbers[i])
            else:
                duplication = self.numbers[i]
                return duplication
            
        return duplication


class Solution_3:
    """
    重排数组：若第i位为m的数 
    比较m和i是否相等 相等则扫描下一个 不相等扫描第m个数和第i个数是否相等
    不相等则交换两个数 相等表示重复
    时间复杂度:O(n) 空间复杂度:O(1)
    输入：
    - numbers:  输入数组

    输出:
    - duplication:  存在重复数字: 输出重复数字
                    输入错误数字: 返回-1
                    不存在错误数字: 返回-2
    """
    def __init__(self, numbers):
        self.numbers = numbers
        self.duplication = -2

    def duplicate(self):
        # S1: 异常处理
        if self.numbers.all()==None or len(self.numbers)<1:
            return -1

        # S2: 异常输入
        if self.numbers.any()<0 or self.numbers.any()>len(self.numbers)-1:
            return -1

        # S3: 重排数组
        for i in range(len(self.numbers)):
            while (self.numbers[i]!=i):
                if self.numbers[i]==self.numbers[self.numbers[i]]:
                    self.duplication=self.numbers[i]
                    return self.duplication
                else:
                    temp = self.numbers[i]
                    self.numbers[i] = self.numbers[temp]
                    self.numbers[temp] = temp
            
        return self.duplication


class Solution_4:
    """
    不修改数组排序 二分查找法变形 【未调试出结果】
    时间复杂度:O(nlogn) 空间复杂度:O(1)
    输入：
    - numbers:  输入数组

    输出:
    - duplication:  存在重复数字: 输出重复数字
                    输入错误数字: 返回-1
                    不存在错误数字: 返回-2
    """
    def __init__(self, numbers):
        self.numbers = numbers
        self.duplication = -2

    def duplicate(self):
        # S1: 异常处理
        if self.numbers.all() == None or len(self.numbers)<1:
            return -1

        # S2: 二分排序
        start = 0
        end = len(self.numbers)-1
        while start<=end:
            middle=(end-start)//2+start
            counter = self.countRange(self.numbers, len(self.numbers), start, middle)
            if end==start:
                if counter>1:
                    return start
                else:
                    break

            if counter>middle-start+1:
                end=middle
            else:
                start=middle+1

        return -2

    def countRange(self, numbers, length, start, end):
        """
        计算数组中元素大于等于start 小于等于end地个数
        """
        if self.numbers.all()==None:
            return 0
        
        count=0
        for i in range(length):
            if numbers[i]>=start and numbers[i]<=end:
                count+=1
        
        return count

