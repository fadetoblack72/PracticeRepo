""""
given a list of numbers "nums", and a target number "target"
finds the indices of the first two numbers in nums whose sum = target
"""
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]



#Checks to see if the given integer, x, is a palindrome

def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else: 
            return (x == int(str(x)[::-1]))

"""
given a sorted array, nums
returns the length of nums with duplicates removed
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            del nums[i]
        else:
            i += 1
    return len(nums)

#problems solved here found at leetcode.com