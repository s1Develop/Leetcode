class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for index, element in enumerate(nums):
            complement = target - element
            if complement in numsDict:
                return [numsDict[complement], index]
            numsDict[element] = index

        return []


# line 5
# 대충 nums 즉 list의 index랑 element를 같이 가져올 수 있게 만든다.

# line 6
# target하는 값에 element값을 뺀 값을 assign한다

# line 7,8
# 그 assigned한 값이 hash안에 들어가 있으면 
# numsDict[complement] 즉 그 값의 index랑 현재 값의 index를 list에 넣어서 return한다

# 아니라면 현재 값을 key로 넣고 그 value를 그 애의 index로 넣는다.