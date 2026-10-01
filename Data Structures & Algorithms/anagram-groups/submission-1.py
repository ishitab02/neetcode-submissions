class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for i in range(len(strs)):
            val = "".join(sorted(strs[i]))
            if val not in seen:
                seen[val] = []
            seen[val].append(strs[i])

        return list(seen.values())