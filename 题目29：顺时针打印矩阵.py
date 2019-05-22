# -*- coding:utf-8 -*-
"""
名称：顺时针打印矩阵
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字；
测试：
"""

# 解题思路：

class Solution:
    def printMatrix(self, matrix):
        """
        顺时针打印矩阵
        输入：
        - matrix: 输入矩阵
        输出：
        - 
        """
        # 异常处理
        if not matrix or len(matrix)<=0 or len(matrix[0])<=0:
            return None

        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        while (rows>start*2 and cols>start*2):
            self.printCircleMatrix(matrix, rows, cols, start, res)
            start += 1
        
        
    def printCircleMatrix(self, matrix, start, rows, cols, res):
        """
        打印一圈
        输入：
        - matrix: 输出矩阵
        - start: 起点
        - rows: 矩阵行数
        - cols: 矩阵列数
        - res: 返回打印队列
        输出：
        - res
        """
        endX = rows - start - 1
        endY = cols - start - 1

        for i in range(start, endX+1):
            res.append(matrix[start][i])
        
        if start<endY:
            for i in range(start+1, endY+1):
                res.append(matrix[i][endY])

        if start<endX and start<endY:
            for i in range(endX-1, start-1, -1):
                res.append(matrix[endY][i])

        if start<endX and start<endY-1:
            for i in range(endY-1,start,-1):
                res.append(matrix[i][start])

        