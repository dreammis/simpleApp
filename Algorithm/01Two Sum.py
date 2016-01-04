nums = [2, 7, 11, 15]
nums.sort()
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index,value in enumerate(nums):
            if target-value in d:
                return d[target-value]+1,index+1
            d[value]=index



class Solution1:
# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		carry = 0
		root = n = ListNode(0)
		while l1 or l2 or carry:
			v1 = v2 = 0
			if l1:
				v1 = l1.val
				l1 = l1.next
			if l2:
				v2 = l2.val
				l2 = l2.next
			carry, val = divmod(v1+v2+carry, 10)
			n.next = ListNode(val)
			n = n.next
		return root.next












s = Solution1()

s.addTwoNumbers(1,2)