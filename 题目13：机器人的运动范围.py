# -*- coding: utf-8 -*-
"""
姓名：机器人的运动范围
问题：机器人从m行n列的矩阵 [0,0] 处开始移动；
     每次只能向左，右，上，下移动一格，不能进入行坐标和数位之和大于k的格子。
测试：功能测试：矩阵为多行多列 threshold为正数
     边界测试：矩阵只有一行或一列 threshold为0
     特殊测试：比较值threshold为负数
"""

class Solution:
    def movingCount(self, matrix, rows, cols, threshold):
        """
        计算能够达到多少格子
        输入：
        - maxtrix： 输入矩阵
        - rows：    矩阵行数
        - cols：    矩阵列数
        - threshold:坐标数位和比较值
        输出：
        - counter： 可以输出多少数字
        """
        if threshold<0 or rows<1 or cols<0:
            return 0
        
        counter = 0
        markMatrix = [False]*(rows*cols)

        counter = self.movingCountCore(matrix, rows, cols, 0, 0, threshold, markMatrix)
        return counter


    def movingCountCore(self, matrix, rows, cols, row, col, threshold, markMatrix):
        """
        计算可能移动的格子
        输入：
        - matrix:   输入矩阵
        - rows:     输入矩阵总行数
        - cols:     输入矩阵总列数
        - row:      检索行数
        - col:      检索列数
        - markMatrix: 统计的计数矩阵
        输出：
        - counter:  格子计数
        """
        value = 0
        if self.check(matrix, rows, cols, row, col, threshold, markMatrix):
            markMatrix[row*cols+col] = True
            value = 1 + self.movingCountCore(matrix, rows, cols, row-1, col, threshold, markMatrix) + \
                        self.movingCountCore(matrix, rows, cols, row+1, col, threshold, markMatrix) + \
                        self.movingCountCore(matrix, rows, cols, row, col-1, threshold, markMatrix) + \
                        self.movingCountCore(matrix, rows, cols, row, col+1, threshold, markMatrix)

        return value
        

    def check(self, matrix, rows, cols, row, col, threshold, markMatrix):
        """
        矩阵值与阈值比较
        输入：
        - matrix:       输入矩阵
        - row:          输入行数
        - col:          输入列数
        - threshold:    比较阈值
        - markMatrix:   矩阵模板
        输出：
        - True/False: 是否大于阈值
        """
        if row>0 and col>0 and row<rows and col<cols \
            and self.getDigitNum(row)+self.getDigitNum(col) < threshold \
            and not markMatrix[row*cols+col]:
            return True

        return False
        

    def getDigitNum(self, number):
        """
        得到数位之和
        输入：
        - number：  输入数字
        输出：
        - sum：     输出数值和
        """
        valSum = 0

        while number>0:
            valSum += number%10
            number = number //10

        return valSum

