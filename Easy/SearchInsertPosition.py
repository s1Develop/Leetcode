class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # one of the constraint is this should be done by O(log(n))
        # So we are going to use binary search

        # endpoint left and right (index)
        l = 0
        r = len(nums)-1

        # <= because all we know is the target is somewhere between l and r including themselves. So when l and r are equal to each other, we still need to do one last check to see if the element at that index is the target.
        while l <= r:

            #set the midpoint (index)
            mid = (l + r) // 2

            # when num[mid] is smaller than the target
            if nums[mid] < target:

                # then left endpoint is now mid + 1
                l = mid + 1
            
            # when num[mid] is greater than the target
            elif nums[mid] > target:

                # then right endpoint is now mid - 1
                r = mid - 1
            
            # when num[mid] is equal to the target number
            else:

                #return that mid which is the index of the target number in num
                return mid
            
        # this means there isn't any target number in num so return l
        return l