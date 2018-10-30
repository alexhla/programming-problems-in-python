class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def hasCycle(self, head):

		if not head or not head.next:
			return False

		slow = head
		fast = head.next

		while slow != fast:
			if fast is None or fast.next is None:
				return False
			fast = fast.next.next
			slow = slow.next

		return True


obj = Solution()

ll = ListNode(5)
ll.next = ListNode(10)
ll.next.next = ListNode(20)
ll.next.next.next = ll

print("Linked List Cycles Present: {}" .format(obj.hasCycle(ll)))