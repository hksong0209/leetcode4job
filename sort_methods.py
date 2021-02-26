# -*- encoding: utf-8 -*-
"""
@File    : sort_methods.py
@Time    : 2020/2/15 10:53
@Author  : hksong
"""
import numpy as np
import time
class SortMethods:
    @staticmethod
    def swap(nums,i,j):
        tmp = nums[i]
        nums[i], nums[j] = nums[j], tmp

    # 冒泡排序
    @staticmethod
    def bubbleSort(nums):
        for i in range(len(nums)):
            for j in range(1, len(nums)-i):
                if nums[j-1] > nums[j]:  # 把大的往上提，最后得升序
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return nums

    # 快速排序
    @staticmethod
    def quickSort(nums):
        def sort_one_number(low, high):
            base = nums[high]  # 选择基准
            i = low # 初始小于base的数的存放位置
            for j in range(low, high):
                if nums[j] < base:  # 此处<和<=对 最终排序结果无影响
                    nums[i], nums[j] = nums[j], nums[i]  # 把找到的第1个小于base的数 放在low处，第二个放在low+1处，....
                    i += 1
            # 遍历完之后，range(low, high)中小于base的数就都被放在 [low, i-1]之间了, [i 之后就都是>=base的数
            nums[i], nums[high] = base, nums[i]  # 把i 作为这个list中第一个取到base的地方
            return i
        def sort_(low, high):
            if low < high:
                index = sort_one_number(low, high)  # 1. 将其中一个数字放至正确位置 2. 该位置左侧的数都<该数；右边的数都>=该数
                sort_(low, index-1)
                sort_(index+1, high)
        sort_(0, len(nums)-1)
        return nums
    # 简版快排
    @staticmethod
    def quickSort2(nums):
        if len(nums) < 2:
            return nums
        else:
            n = 0
            for i in range(0, len(nums)-1):
                if nums[i] < nums[-1]:
                    nums[n], nums[i] = nums[i], nums[n]
                    n += 1
            return SortMethods.quickSort2(nums[0:n]) + [nums[-1]] + SortMethods.quickSort2(nums[n:len(nums)-1])

    # 选择排序  => 与冒泡不同是每轮只交换一次 即进行一次选择，但每次选择的方法是遍历
    @staticmethod
    def selectSort(nums):
        for i in range(len(nums)):
            idx = i
            for j in range(i + 1, len(nums)):  # 找第i小的数的idx
                if nums[j] < nums[idx]:
                    idx = j
            nums[i], nums[idx] = nums[idx], nums[i]  # 每轮交换一次
        return nums

    # 堆排序
    # 【完全二叉树】的性质，根节点从0开始编号，某父节点编号为n, 则其左孩子为2n+1
    # 最大堆，树中任意父节点的值 >= 左右孩子节点的值
    #
    @staticmethod
    def heapSort(nums):
        def heapfy(n, i_father):  # 对nums[:n]进行最大堆化
            i_left, i_right, index_max = 1 + i_father * 2, 2 + i_father * 2, i_father
            if i_left < n and nums[i_left] > nums[index_max]:
                index_max = i_left
            if i_right < n and nums[i_right] > nums[index_max]:
                index_max = i_right
            if index_max != i_father:
                nums[i_father], nums[index_max] = nums[index_max], nums[i_father]  # 交换 父节点 和 子节点 值
                heapfy(n, index_max)  # 以更新后的子节点为父节点 使其保持大顶堆

        # 初始化大顶堆， 使每个节点都满足大顶堆， 且最大值在数组首位
        for i in range(len(nums)-1, -1, -1):
            heapfy(len(nums), i)

        # 通过heafi来寻找子序列最大值nums[0]，而不是通过遍历（普通选择排序）
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapfy(i, 0)  # 子序列长度变为i
        return nums

    # 归并排序
    # 先将所有元素，拆到最细的单个元素
    # 然后不断两两合并 相邻的有序子序列
    @staticmethod
    def mergeSort(nums):
        # 合（将两个有序数组合并成一个有序数组）
        def merge_(part0, part1):
            i, j, pp = 0, 0, []
            while i < len(part0) and j < len(part1):
                if part0[i] <= part1[j]:
                    pp.append(part0[i])
                    i += 1
                else:
                    pp.append(part1[j])
                    j += 1
            pp.extend(part0[i:])
            pp.extend(part1[j:])
            return pp
        # 分（一直拆到单个数字）
        def sort_(nums=nums):
            if len(nums) < 2:
                return nums
            idx_mid = len(nums) // 2
            part0, part1 = sort_(nums[:idx_mid]), sort_(nums[idx_mid:])
            # 直到2个merge_sort都return回结果（最底层返回单个数字,后来都是有序列表）
            return merge_(part0, part1)
        return sort_()


    @staticmethod
    def test_single_method(method_str, method, nums, ans):
        start = time.time()
        res = method([n for n in nums])
        for i in range(30):
            method([n for n in nums])
        runtime = time.time()-start
        tf = (res == ans)
        print("%s: %s | %.4f" % (method_str, str(tf), runtime))

    @staticmethod
    def test_all_method(*args):
        if len(args)==1:
            nums = args[0]
        else:
            nums = [int(n) for n in np.random.randint(low=0, high=100, size=np.random.randint(30, 500))]
            ans = [n for n in nums]
            ans.sort()
        print("\nori list len: %d" % len(nums))
        #print("ori list: %s\n" % ",".join([str(n) for n in nums]))
        SortMethods.test_single_method("bubbleSort", SortMethods.bubbleSort, nums, ans)
        SortMethods.test_single_method("quickSort", SortMethods.quickSort, nums, ans)
        SortMethods.test_single_method("quickSort2", SortMethods.quickSort2, nums, ans)
        SortMethods.test_single_method("selectSort", SortMethods.selectSort, nums, ans)
        SortMethods.test_single_method("heapSort", SortMethods.heapSort, nums, ans)
        SortMethods.test_single_method("mergeSort", SortMethods.mergeSort, nums, ans)


nums_in = []
print(SortMethods.test_all_method())
nums = [3,1,2,4,7,5,6,0,9]
# def getIndex(low, high):
#     base = nums[low]
#     while low < high:
#         while low < high and nums[low] < base:
#             low += 1
#         while low < high and nums[high] >= base:
#             high -= 1
#         nums[low], nums[high] = nums[high], nums[low]
#     return low
# getIndex(0, len(nums)-1)
# print(nums)


def heapfi(i_father):  # 使父左右保持大顶堆
    i_left, i_right, index_max = 1 + i_father * 2, 2 + i_father * 2, i_father
    if i_left < len(nums) and nums[i_left] > nums[index_max]:
        index_max = i_left
    if i_right < len(nums) and nums[i_right] > nums[index_max]:
        index_max = i_right
    if index_max != i_father:
        nums[i_father], nums[index_max] = nums[index_max], nums[i_father]  # 交换 父节点 和 子节点 值
        heapfi(index_max)  # 以更新后的子节点为父节点 使其保持大顶堆


# 初始化大顶堆 ， 使每个节点都满足大顶堆， 且最大值在数组首位
for i in range(len(nums), -1, -1):
    heapfi(i)
print(nums)


###############################
nums = [3,1,2,4,7,5,6,0,9]
def quickS(nums):
    def sort_(start=0, end=len(nums)-1):
        if start < end:
            imid = parti_one(start, end)
            sort_(start, imid-1)
            sort_(imid+1, end)
    def parti_one(start, end):
        i = start
        base = nums[end]
        for j in range(start, end):
            if nums[j]<base:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        nums[i], nums[end] = nums[end], nums[i]
        return i
    sort_()

def merge_sort(nums):
    # 合（将两个有序数组合并成一个有序数组）
    def merge_(part0, part1):
        i, j, pp = 0, 0, []
        while i<len(part0) and j<len(part1):
            if part0[i] <= part1[j]:
                pp.append(part0[i])
                i += 1
            else:
                pp.append(part1[j])
                j += 1
        pp.extend(part0[i:])
        pp.extend(part1[j:])
        return pp
    # 分（一直拆到单个数字）
    def sort_(nums=nums):
        if len(nums) < 2:
            return nums
        idx_mid = len(nums)//2
        part0, part1 = sort_(nums[:idx_mid]), sort_(nums[idx_mid:])
        # 直到2个merge_sort都return回结果（最底层返回单个数字,后来都是有序列表）
        return merge_(part0, part1)
    return sort_()


print("归并排序")
print(merge_sort(nums))


#
# quickS(nums)

