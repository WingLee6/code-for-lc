# -*- coding: utf-8 -*-
# @Time    : 2022/7/10 10:42 PM
# @Author  : lee
# @FileName: q26_删除有序数组中的重复项.py
# @Desc    :


"""
26. 删除有序数组中的重复项

给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
元素的 相对顺序 应该保持 一致 。
由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。
更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k 个元素应该保存最终结果。
将最终结果插入 nums 的前 k 个位置后返回 k 。
不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

判题标准:
系统会用下面的代码来测试你的题解:

int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有断言都通过，那么您的题解将被 通过。

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 方法一，整理成集合，在转换为列表
        # P.S. LeetCode在线编辑无法通过
        # return len(list(set(nums)))

        # 方法二：快慢指针法
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        return slow + 1




if __name__ == '__main__':
    input = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    result = solution.removeDuplicates(nums=input)
    print(result)





"""
示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

"""