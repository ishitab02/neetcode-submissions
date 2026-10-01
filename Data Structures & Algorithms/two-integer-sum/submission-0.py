class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #A nested loop is fine, but it searches the list multiple times, so instead we can use a hash map or dictionary
        seen = {}

        #loop
        for i in range(len(nums)):
            #find complement
            complement = target - nums[i]
            #if complement exists in seen
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i