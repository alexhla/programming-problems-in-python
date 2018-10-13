class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def mergeTwoLists(self, l1, l2):

		head = ListNode(0)
		curr = head

		while l1 != None or l2 != None:

			if l1 != None and l2 != None:
				if l1.val < l2.val:
					curr.next = ListNode(l1.val)
					curr = curr.next
					l1 = l1.next if l1!=None else l1
					continue
				else:
					curr.next = ListNode(l2.val)
					curr = curr.next
					l2 = l2.next if l2!=None else l2
					continue

			if l1 == None:
				curr.next = ListNode(l2.val)
				curr = curr.next
				l2 = l2.next if l2!=None else l2
				continue

			if l2 == None:
				curr.next = ListNode(l1.val)
				curr = curr.next
				l1 = l1.next if l1!=None else l1
				continue                      

		return head.next

obj = Solution()

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)

n2 = ListNode(4)
n2.next = ListNode(5)
n2.next.next = ListNode(6)

ans = obj.mergeTwoLists(n1,n2)

print("\nAnswer Is ", end="")
while ans != None:
	print(ans.val, end="")
	ans = ans.next

print("\n")