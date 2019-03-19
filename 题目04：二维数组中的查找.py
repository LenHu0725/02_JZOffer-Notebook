# -*- coding: utf-8 -*-
"""
名称:   二维数组中的查找
题目:   在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
测试:   数组中包含查找的数字(查找数字为最大/最小值；查找数字为中间值)
        数组中不包含查找数字(小于最小值 大于最大值 最大最小的中间值)
        特殊输入测试(空指针)
"""


class Solution_1:
    def __init__(self):
        pass

    def find(self, target, array):
        """
        二层遍历 
        时间复杂度:O(n^2) 空间复杂度:O(1)
        
        输入：
        - target: 寻找的数值
        - array: 查找的矩阵
        输出:
        - Bool: array中是否包含target
        """
        # S1: 异常处理
        if array.all()==None:
            # rasie Exception("输入矩阵为空")
            return False

        # S2: 获得array的长宽
        n, m = len(array), len(array[0])

        # S3: 二层遍历
        for i in range(n):
            for j in range(m):
                if array[i][j]==target:
                    return True
        return False




class Solution_2:
    def __init__(self):
        pass

    def find(self, target, array):
        """
        从右上到左下逐渐排除
        时间复杂度:O(n) 空间复杂度:O(1)
        
        输入：
        - target: 寻找的数值
        - array: 查找的矩阵
        输出:
        - Bool: array中是否包含target
        """
        # S1: 异常输入
        if array.all()==None:
            return False
        # S2: 获得array大小
        row, col = array.shape
        i = 0
        j = col-1

        # S3: 右上到左下遍历
        while(i<row and j>=0):
            # 判断大小
            if array[i][j]>target:
                j-=1
            elif array[i][j]<target:
                i+=1
            else:
                return True

        return False



