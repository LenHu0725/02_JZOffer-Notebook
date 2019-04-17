# -*- coding:utf-8 -*-
"""
名称：二进制中1的个数
题目：输入一个整数，输出该数二进制表示中1的个数，负数用补码表示。
测试：正数：0 - 0X7FFFFFFF
     负数：0X800000 - 0XFFFFFFFF
     0
"""

class Solution:
    # python 的左移和右移命令为 "<<" ">>"
    def NumberOf1(self, n):
        """
        左移和1相比较 - 可能陷入死循环
        输入：
        - n：输入整数
        输出：
        - count：n的二进制有多少
        """

        # S1:转换为补码计算 正数的补码为本身 负数的补码为
        counter = 0

        if n==0:
            return 0

        elif n==-1:
            return 1

        # S2:数值右移
        while (n!=0) and (n!=-1):
            
            if (n & 1)==1:
                counter += 1
            
            n = n>>1
        
        return counter



    # def NumberOf2(self, n):
    #     """
    #     数值最后一位比较 无法使用
    #     输入：
    #     - n：输入整数
    #     输出：
    #     - counter：n的二进制有多少
    #     """
        
    #     counter = 0

    #     while (n!=0) and (n!=-1):
    #         if n%2 == 1:
    #             counter += 1

    #         if n!=-1:
    #             n = n>>1
    #         else:
    #             break

    #     return counter



    def NumberOf3(self, n):
        """
        给面试官带来惊喜的做法
        输入：
        - n：输入整数
        输出：
        - counter：n的二进制有多少
        """
        
        counter = 0

        # 若为负数 应0xff相与 去除负数影响
        if n < 0:
            n = n & 0xfffffffff

        while(n):
            n = (n-1) & n
            counter += 1

        return counter



    def NumberOf4(self, n):
        """
        利用python的机制
        输入：
        - n：输入整数
        输出：
        - counter：n的二进制有多少
        """
        return bin(n & 0Xffffffff).count("1")


# 功能测试
test_list = [0, 5, 0X7FFFFFFF, 0X800000, -3, 0XFFFFFFFF]

I = Solution()

for _ in test_list:
    c = I.NumberOf3(_)
    print("Test Number is : {}, Result is {}".format(_, c))