class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        current = self
        nodes = []
        while current:
            nodes.append(str(current.val))
            current = current.next
        return " -> ".join(nodes) + " -> None"


def solution(head: ListNode) -> ListNode | None:
    cter = 1
    current = head
    while current:
        current = current.next
        cter += 1
    print(f"done after {cter}.")
    mid = cter // 2
    current = head
    while current.next:
        if current.val == mid:
            return current
        current = current.next
    raise ValueError("Could not figure solution")


def solution_2(head: ListNode) -> ListNode | None:
    slow = head.next
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    h = ListNode(val=1)
    current = h
    for i in range(2, 6):
        current.next = ListNode(val=i)
        current = current.next
    # print(solution(head=h))
    print(solution_2(head=h))
    current = h
    for i in range(2, 7):
        current.next = ListNode(val=i)
        current = current.next
    print(solution_2(head=h))
