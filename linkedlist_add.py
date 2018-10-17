class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def addNumbers(self, l1, l2):    
		carry = 0
		head = ListNode(0)  # create head node
		curr = head

		while l1 != None or l2 != None:

			v1 = l1.val if l1!=None else 0
			v2 = l2.val if l2!=None else 0

			n = v1 + v2 + carry
			carry = 0

			if n >= 10:
				carry = n//10
				n %= 10
				

			curr.next = ListNode(n)
			curr = curr.next

			l1 = l1.next if l1!=None else l1
			l2 = l2.next if l2!=None else l2

		if carry > 0:
			curr.next = ListNode(carry)

		return head.next

obj = Solution()

n1 = ListNode(5)
n1.next = ListNode(10)
n1.next.next = ListNode(20)

n2 = ListNode(5)
n2.next = ListNode(10)
n2.next.next = ListNode(20)

ans = obj.addNumbers(n1,n2)

print("\nAnswer Is ", end="")
while ans != None:
	print(ans.val, end="")
	ans = ans.next

print("\n")