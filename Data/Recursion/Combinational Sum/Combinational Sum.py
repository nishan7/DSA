'''
#### Name:  Combinational Sum
Link: [link]()

'''



def combinationSum(candidates, target):
    result = []
    candidates = sorted(candidates)
    def dfs(remain, stack):
        if remain == 0:
            result.append(stack)
            return 

        for item in candidates:
            if item > remain: break
            if stack and item < stack[-1]: continue
            else:
                dfs(remain - item, stack + [item])

    dfs(target, [])
    return result


nums = [1,2,5] 
print(combinationSum(nums, 5))


# No repeat

class Solution(object):
    def combinationSum2(self, candidates, target):
        ret = []
        self.dfs(sorted(candidates), target, 0, [], ret)
        return ret
    
    def dfs(self, nums, target, idx, path, ret):
        if target <= 0:
            if target == 0:
                ret.append(path)
            return 
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], ret)