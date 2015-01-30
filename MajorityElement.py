# solution to Majority Element problem at https://oj.leetcode.com/problems/majority-element/
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
		# maintain a list of numbers found to not be the Majority element
        alreadyChecked = []
        for i in num:
            count = 0
			# don't go through the loop for confirmed non-answers
            if i in alreadyChecked:
                continue
            for j in num:
                if i == j:
                    count += 1
					# stop checking as soon as the answer has been found
                    if count > (len(num) / 2):
                        return i
            alreadyChecked.append(i)