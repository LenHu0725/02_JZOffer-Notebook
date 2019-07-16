"""
名称：1～n整数中1出现的次数
题目：输入一个整数n,求1~n这n个整数的十进制表示中1出现的次数。
     例如，输入12，1~12这些整数中包含1的数字有1，10，11，12一共出现了5次。
测试：功能测试：输入5、10、55、99等；
     边界测试：输入 0、1等
     性能测试：较大数字 10000、21235；
"""

# 思路1: 暴力查找数字个数
class Solution1:
    def NumberOf1Between1AndN_Solution(self, n):
        totalCounter = 0

        for i in range(1, n+1):
            totalCounter += self.NumberOf1Core(i)

        return totalCounter

    
    def NumberOf1Core(self, number):
        counter1 = 0

        while number:
            if number%10 == 1:
                counter1 += 1

            number /= 10
        
        return counter1


# 思路2: 查看1出现的规律
class Solution2:
    def get_1_digits(self, n):
        """
        获取每个位数之间1的总数
        :param n: 位数
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        current = 9 * self.get_1_digits(n-1) + 10 ** (n-1)

        return self.get_1_digits(n-1) + current


    def get_1_nums(self, n):

        if n < 10:
            return 1 if n >= 1 else 0

        digit = len(str(n))  # 位数
        low_nums = self.get_1_digits(digit-1)  # 最高位之前的1的个数
        
        high = int(str(n)[0])  # 最高位
        low = n - high * 10 ** (digit-1)  # 低位

        if high == 1:
            high_nums = low + 1  # 最高位上1的个数
            all_nums = high_nums
        else:
            high_nums = 10 ** (digit - 1)
            all_nums = high_nums + low_nums * (high - 1)  # 最高位大于1的话，统计每个多位数后面包含的1
        
        return low_nums + all_nums + self.get_1_nums(low)
