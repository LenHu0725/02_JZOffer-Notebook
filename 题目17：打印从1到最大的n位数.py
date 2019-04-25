# -*- coding:utf-8 -*-
"""
名称：打印从1到最大的n位数
题目：输入数字n,按顺序打印出从1到最大的n位十进制数；
     比如输入3，则打印出1、2、3一直到最大的3位数999；
测试：功能测试：输入 1、2、3、...
     边界测试：-1、0、...
"""


class Solution1:
    def printMax(self, n):
        """ 暴力法输出数值
        输入：
        - n：输出位数
        """
        for i in range(10 ** n):
            print( i )



# 需要注意 题目未规定最大数范围直接打印数字会超出范围
# 将问题转换为打印字符串即可
## 1.字符串中做加法；
## 2.打印字符串；

class Solution2:
    def Print1ToMaxOfNDigits(self, n):
        if n<=0:
            return 
        number = ['0']*n
        while not self.Increment(number):
            self.PrintNumber(number)



    def Increment(self, number):
        """ 加1操作与溢出判断
        输入：
        - number：输入数字
        输出：
        - Bool：True \ False
        """
        isOverFlow = False
        nTakeOver = 0
        nLength = len(number)

        for i in range(nLength-1, -1, -1):
            nSum = int(number[i]) + nTakeOver
            if i == nLength - 1:
                nSum += 1

            if nSum >= 10:
                if i == 0:
                    isOverFlow = True
                else:
                    nSum -= 10
                    nTakeOver = 1
                    number[i] = str(nSum)
            else:
                number[i] = str(nSum)
                break
            
        return isOverFlow



    def PrintNumber(self, number):
        """ 打印数字
        输入：
        - number：打印数字
        """
        isBeginning0 = True
        nLength = len(number)

        for i in range(nLength):
            if isBeginning0 and number[i] != '0':
                isBeginning0 = False
            if not isBeginning0:
                print('%c'% number[i], end='')
        print('')


    
    def Print1ToMaxOfNDigits2(self, n):
        if n <= 0:
            return

        number = ['0']*n
        for i in range(10):
            number[0] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(number, n, 0)



    def Print1ToMaxOfNDigitsRecursively(self, number, length, index):
        if index == length - 1:
            self.PrintNumber(number)
            return 

        for i in range(10):
            number[index+1] = str(i)
            self.Print1ToMaxOfNDigitsRecursively(number, length, index+1)



if __name__ == "__main__":
    import time

    strTime = time.time()

    # pr = Solution1()
    # pr.printMax(3)
    pr = Solution2()
    pr.Print1ToMaxOfNDigits(3)

    endTime = time.time()
    
    print("Run time is {} !".format(endTime-strTime))