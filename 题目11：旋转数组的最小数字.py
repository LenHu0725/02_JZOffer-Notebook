# -*- coding:utf-8 -*-
"""
名称：旋转数组的最小数字
题目：递增排序数组的旋转并输出数组的最小值
     Eg. [1,2,3,4,5] -> [3,4,5,1,2]
测试：Eg.[5,6,7,8,9,10,3,4], [3,4,5,6], [1,1,0,1,1]
"""

class Solution:
     """
     二分查找
     指针1、指针2从两头向中间移动 中间指针位于中位数数值I
     若I小于指针1 2 的数值 说明旋转数组最小值在中位数左边 指针2为中位数数值
     若I小于指针1 2 的数值 说明旋转数组最小值在中位数左边 指针1为中位数数值
     输入：
     - arr: 需要求得的数组
     输出：
     - 最小数数值
     """
     def minNumberInRoatteArray(self, arr):
          #S0: 异常和特殊情况处理
          if not arr:
              return None
          if len(arr)==0 :
               return 0
          elif len(arr)==1:
               return 1

          #S1: 指针初始化
          index_1 = 0
          index_2 = len(arr)-1
          indexMed = index_1

          while (index_2-index_1) > 1:
               if arr[indexMed]<=arr[index_1] and arr[indexMed]<arr[index_2]:
                    index_2 = indexMed
               elif arr[indexMed]>arr[index_1] and arr[indexMed]>arr[index_2]:
                    index_1 = indexMed
               elif arr[index_1]==arr[index_2]:
                    index_2 = self.seqSearch(arr)
                    break
               else:
                    print(index_1, index_2)

               indexMed = (index_1+index_2) // 2
          return arr[index_2]

     def seqSearch(self, arr):
          """
          顺序查找
          当出现[1,1,1,0,1]，[1,0,1,1,1]时无法确定中间指针 仅能顺序查找
          输入：
          - arr: 输出数组
          输出：
          - 最小数值
          """
          arrLen = len(arr)
          arrIndex = arrLen-1
          minVal = arrLen-1
          while arrIndex>0:
               if arr[arrIndex]<arr[minVal]:
                    minVal = arrIndex
               elif arr[arrIndex]==arr[minVal]:
                    pass
               elif arr[arrIndex]>arr[minVal]:
                    break
               arrIndex-=1

          return minVal


# lArr = [5,6,7,8,9,10,3,4]
lArr = [2,2,2,1,2,2]
l = Solution()
print(l.minNumberInRoatteArray(lArr))
