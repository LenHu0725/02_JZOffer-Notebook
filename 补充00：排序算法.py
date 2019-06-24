# -*- coding:utf-8 -*-
"""
名称：  排序算法
题目：  插入排序 冒泡排序 归并排序 快速排序 希尔排序法 直接选择 堆排法 基数排序
"""

# 1. 快速排序
class quickSortList:
    """
    快速排序 分而治之
    推荐视频：【B站】av47837026
    输入：
    - alist: 排序数组
    输出：
    - alist: 排序后的数组
    """   
    def sort(self, alist, left, right):

        pivot = alist[right]  # 定义pivot
        i = left-1
        for j in range(left, right):
            if alist[j]<pivot:
                i+=1
                alist[i], alist[j] = alist[j], alist[i]

        alist[right], alist[i+1] = alist[i+1], alist[right]
        return i+1

    def quick_sort(self, alist, left, right):
        if left<right:
            pivot_index = self.sort(alist, left, right)
            self.quick_sort(alist, left, pivot_index-1)
            self.quick_sort(alist, pivot_index+1, right)
        
        return alist

l = [4, 2, 6, 9, 3, 7, 10, 8]
l2= [4, 2, 6, 9, 3, 7]
s = quickSortList()
print(s.quick_sort(l, 0, len(l)-1))
