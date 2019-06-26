"""
名称：最小的k个数
题目：输入n个整数，找出其中最小的K个数。
     例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
测试：功能测试：输入数组中有相同数字，输入数组中没有相同数字；
     边界测试：输入k等于1或等于数组长度
     特殊测试：k小于1，k大于数组长度，nums为Null
"""

# 思路1：快速排序选择前K个数
def Solution_1():
    def sort(self, nums, left, right):
        """ sort """
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j]<pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            
        nums[i+1], nums[pivot] = nums[pivot], nums[i+1]
        return  i+1

    def quickSort(self, nums, left, right):
        """ Quick Sort """
        if left < right:
            pivot_index = self.sort(nums, left, right)
            self.quickSort(nums, left, pivot_index-1)
            self.quickSort(nums, pivot_index+1, right)

        return nums

    def selectK(self, nums, k):
        """ 
        快速排序选择
        Input:
        - nums: 序列
        - k：前k个数
        Output：
        - kNums：前k个数值序列
        """
        # S0：异常处理
        if not nums or len(nums)<k or k<1:
            return False

        # S1: 快排
        nums = self.quickSort(nums, 0, len(nums)-1)

        # S2: 返回前k个数
        return nums[:k]

