"""
全排列算法（0-1，P4）

随机生成不重复的数列，当数列内数字排序正确再输出。
一个非常低效的算法。
"""
from random import randint
from time import time

def gen_arr(n):
    arr = []
    for _ in range(n):
        while True:
            random_int = randint(1, 1000000)
            if random_int not in arr:
                break
        arr.append(random_int)
    return arr

def check_arr(arr):
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            return False
    return True

def full_sort(n):
    arr_list = []
    while True:
        arr = gen_arr(n)
        if arr not in arr_list:
            arr_list.append(arr.copy)
        else:
            continue
        if check_arr(arr):
            return arr

n = int(input('Please input the length of the array: '))
start_time = time()
arr = full_sort(n)
end_time = time()
print(arr)
print('Elapse time: %s s' % (end_time - start_time))