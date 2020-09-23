"""
数组（1-3，P16）

访问数据简单，但增删数据费时。
访问时间复杂度O(1)，新增数据最大（在头部）时间复杂度O(n)，删除同理。
"""

class Array():
    def __init__(self):
        self.array = dict()
    
    def read(self, i):
        return self.array[i]
    
    def read_all(self):
        return self.array
    
    def add(self, value, position=None):
        if position is None:
            position = len(self.array)
        if len(self.array) == 0:
            self.array[0] = value
            return 0
        for i in range(len(self.array), position, -1):
            self.array[i] = self.array[i-1]
        self.array[position] = value
        return 0
    
    def delete(self, position=None):
        if position is None:
            position = len(self.array)-1
        for i in range(position, len(self.array)-1):
            self.array[i] = self.array[i+1]
        del self.array[len(self.array)-1]

arr = Array()
arr.add('Blue')
arr.add('Yellow')
arr.add('Red')
print(arr.read_all())

# 访问数据
print(arr.read(2))

# 添加数据
arr.add('Green', 1)
print(arr.read_all())

# 删除数据
arr.delete(1)
print(arr.read_all())