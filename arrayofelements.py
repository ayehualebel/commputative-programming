class Solution(object):
    def rearrangeArray(self, nums):
        self.nums=nums
        nums.sort()
        for i in range(1,len(nums)-1,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums
        
