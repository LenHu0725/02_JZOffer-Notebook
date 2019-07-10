"""
名称：数据流重的中位数
题目：如何得到一个数据流中的中位数？
     如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
     如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
测试：功能测试：从数据流中读出奇数个数字，从数据流中读出偶数个数字；
     边界测试：从数据流中读出 0、1、2 个数字；
     负面测试：
"""

# 解题思路：构建最大最小堆
def Solution():
    
    def __init__(self):
        self.left = None
        self.right = None
        self.count = 0


    def insert(self, num):
        if self.count & 1 == 0:
            self.left.append(num)
        else:
            self.right.append(num)

        self.count += 1


    def getMedia(self, x):
        if self.count == 1:
            return self.left[0]

        self.maxHeap(self, self.left)
        self.minHeap(self, self.right)

        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]

        self.maxHeap(self, self.left)
        self.minHeap(self, self.right)

        if self.count & 1 == 0:
            return (self.left[0] + self.right[0])/2.0
        else:
            return self.left[0]


    def maxHeap(self, alist):
        length = len(alist)
        
        if alist == None or length <= 0:
            return None
        if length == 1:
            return alist

        for i in range(length//2-1, -1, -1):
            k = i, temp = alist[k]; heap = False
            while not heap and 2*k < length-1:
                index = 2*k+1

                if index < length -1:
                    if alist[index] < alist[index + 1]: index += 1
                
                if temp >= alist[index]: heap = True
                else:
                    alist[k] = alist[index]
                    k = index

                alist[k] = temp


    def minHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist

        for i in range(length//2-1, -1, -1):
            k = i; temp = alist[k]; heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k+1

                if index < length - 1:
                    if alist[index] > alist[index + 1]: index += 1

                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index

            alist[k] = temp


