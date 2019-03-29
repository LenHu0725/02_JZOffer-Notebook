# -*- coding:utf-8 -*-
"""
名称：用两个栈实现队列
题目：用两个栈实现一个队列，队列声明如下:
     请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部插入节点和在队列头部删除节点的功能；
     [理解：用两个栈实现一个队列，完成队列的Push和Pop，队列中元素为int]
测试：非空的队列删除添加元素
     空的队列删除添加元素
     删除队列的元素直到空
"""

# 解题思路：
# 暴力循环法 仅利用B存储A的元素；
import time

class Solution_1:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]

    def push(self, node):
        """
        压入堆栈
        输入：
        - node: 压入元素
        """
        self.stackA.append(node)

    def pop(self):
        """弹出数据"""
        if len(self.stackA)==0:
            print("stack is None!")
            return None
        else:
            while len(self.stackA)!=1:
                self.stackB.append(self.stackA.pop())
            pop = self.stackA.pop()
            while len(self.stackB)!=0:
                self.stackA.append(self.stackB.pop())
            return pop


# 解题思路：
# A用做堆栈【顺序为存入顺序】 B用做出栈【顺序与存入顺序相反】

class Solution_2():
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        self.stackA.append(node)

    def pop(self):
        # S1: 先判断B中是否有数
        if self.stackB:
            self.stackB.pop()
        # S2: A和B中都没数
        elif not self.stackA:
            return None
        # S3: A中有数向B转移
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


# 测试1：
tSta = time.time()
stack = Solution_1()
stack.push(1); stack.push(3); stack.push(5); stack.push(46); stack.push(7);
print("\nStack is : ", stack.stackA)
stack.pop(); stack.pop()
print("Final Stack is : ", stack.stackA, stack.stackB[::-1])
tEnd = time.time()
print("Spend Time is : ", tEnd-tSta)

# 测试2:
tSta = time.time()
stack = Solution_2()
stack.push(1); stack.push(3); stack.push(5); stack.push(46); stack.push(7);
print("\nStack is : ", stack.stackA)
stack.pop(); stack.pop()
print("Final Stack is : ", stack.stackA, stack.stackB[::-1])
tEnd = time.time()
print("Spend Time is : ", tEnd-tSta)



# 扩展：用两个队列形成栈
class Solution_3:
    def __init__(self):
        self.queueA = []
        self.queueB = []

    def push(self, node):
        self.queueA.insert(0, node)

    def pop(self):
        if not self.queueA:
            return None
        
        while len(self.queueA)!=1:
            self.queueB.insert(0, self.queueA.pop())
        self.queueA, self.queueB = self.queueB, self.queueA
        return self.queueB.pop()


# 测试
tSta = time.time()
queue = Solution_3()
queue.push(1); queue.push(3); queue.push(7); queue.push(9); queue.push(10)
print("\nQueue is : ", queue.queueA)
queue.pop(); queue.pop(); queue.pop()
print("Queue is : ", queue.queueA)
tEnd = time.time()
print("Spend time is : ", tEnd-tSta)
