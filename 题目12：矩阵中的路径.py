# -*- coding:utf-8 -*-
"""
名称：矩阵中的路径
题目：设计函数 判断矩阵中是否包含某字符串的路径；
     路径从矩阵中任意格子开始，每步向左 向右 向上 向下 移动一个格子；
测试：功能测试：多行多列矩阵 存在或不存在路径
     边界测试：矩阵只有一行或一列 矩阵和路径的字母都是相同的
     特殊测试：输入空指针
"""

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        """ 
        查找 matrix[row, col]下一个 是否为 strs[i]的字符
        输入：
        - matrix:  输入数组;
        - row:  选定行;
        - col:  选定列;
        - s:    下一个字符;
        输出：
        - next: -1未找到下一个字符 1上 2右 3下 4左
        """
        if not matrix or rows<0 or cols<0 or path==None:
            return False

        markMatrix = [0]*(rows*cols)
        pathIndex = 0

        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, pathIndex, markMatrix):
                    return True

        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, pathIndex, markMatrix):
        """
        查找字符序列起点
        输入：
        - matrix: 输入矩阵
        - rows: 所有行数
        - cols: 所有列数
        - row:  索引行数
        - col:  索引列数
        - path: 路径字符
        - pathIndex: 路径字符序号
        - markMatrix: 路径标记
        输出：
        - Bool: 是否存在路径
        """
        if pathIndex == len(path):
            return True

        if row>=0 and row<rows and col>0 and col<cols and matrix[row*cols+col]==path[pathIndex] and not markMatrix[row*cols+col]:
            pathIndex+=1
            markMatrix[row*cols+col] = True
            hasPath = self.hasPathCore(matrix, rows, cols, row+1, col, path, pathIndex, markMatrix) or \
                      self.hasPathCore(matrix, rows, cols, row-1, col, path, pathIndex, markMatrix) or \
                      self.hasPathCore(matrix, rows, cols, row, col+1, path, pathIndex, markMatrix) or \
                      self.hasPathCore(matrix, rows, cols, row, col-1, path, pathIndex, markMatrix)
            if not hasPath:
                pathIndex -=1
                markMatrix[row*cols+col]=False

        return hasPath
