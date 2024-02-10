# this is a text format

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        save = list.copy(nums)
        for i in range(0,len(nums)):
            save.pop(i)
            if((target-nums[i]) in save):
                ret.append(i)
            save = list.copy(nums)
          
        return ret