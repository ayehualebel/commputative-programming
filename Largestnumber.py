class Solution(object):
    def largestNumber(self, nums):
        self.nums=nums
        nums=[str(num) for num in nums]
        nums.sort(key=lambda x: x * 10, reverse=True)
        largest_num = ''.join(nums)
        return largest_num if largest_num[0] != '0' else '0'
