"""
选择排序（0-1，P2）

在第n轮，在第n个数字后查找最小的数字，并与第n个数字交换。
时间复杂度为O(n^2)。
"""

from random import randint
from time import time

def gen_arr(n):
    arr = []
    for _ in range(n):
        # while True:
        random_int = randint(1, 1000000)
            # if random_int not in arr:
            #     break
        arr.append(random_int)
    return arr

def check_arr(arr):
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            return False
    return True

def selection_sort(arr):
    for i in range(len(arr)):
        min_num = min(arr[i:])
        for j in range(i, len(arr)):
            if arr[j] == min_num:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

n = int(input('Please input the length of the array: '))
arr = gen_arr(n)
start_time = time()
arr = selection_sort(arr)
end_time = time()
print(arr)
print(check_arr(arr))
print('Elapse time: %s s' % (end_time - start_time))