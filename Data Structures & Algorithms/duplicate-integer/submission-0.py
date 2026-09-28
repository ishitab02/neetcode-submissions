class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #initialise a set for seen elements
        seen = set()

        #loop through the array to see if the element is there
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            # then add the element to the list
            seen.add(nums[i])
        return False