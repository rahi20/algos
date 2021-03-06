#Easy Prob 26:  Remove Duplicates from Sorted Array

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n == 1 or n == 0 :
            return n

        k = n 
        i = n - 1
        while i >= 0:

            nbr_dup = 0
            while i!= 0 and nums[i] == nums[i - 1]: 
                nbr_dup += 1
                i -= 1
                k -= 1 
            if nbr_dup != 0:
                nums[ i : ] = nums[ i + nbr_dup : ]
            
            i -= 1 

        return k


sol = Solution()
# print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(sol.removeDuplicates([-50,-50,-49,-48,-47,-47,-47,-46,-45,-43,-42,-41,-40,-40,-40,-40,-40,-40,-39,-38,-38,-38,-38,-37,-36,-35,-34,-34,-34,-33,-32,-31,-30,-28,-27,-26,-26,-26,-25,-25,-24,-24,-24,-22,-22,-21,-21,-21,-21,-21,-20,-19,-18,-18,-18,-17,-17,-17,-17,-17,-16,-16,-15,-14,-14,-14,-13,-13,-12,-12,-10,-10,-9,-8,-8,-7,-7,-6,-5,-4,-4,-4,-3,-1,1,2,2,3,4,5,6,6,7,8,8,9,9,10,10,10,11,11,12,12,13,13,13,14,14,14,15,16,17,17,18,20,21,22,22,22,23,23,25,26,28,29,29,29,30,31,31,32,33,34,34,34,36,36,37,37,38,38,38,39,40,40,40,41,42,42,43,43,44,44,45,45,45,46,47,47,47,47,48,49,49,49,50]))
