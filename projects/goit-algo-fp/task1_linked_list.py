class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous

    def get_middle(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, left, right):
        if left is None:
            return right

        if right is None:
            return left

        if left.data <= right.data:
            result = left

            result.next = self.sorted_merge(
                left.next,
                right
            )
        else:
            result = right

            result.next = self.sorted_merge(
                left,
                right.next
            )

        return result

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)

        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        return self.sorted_merge(left, right)

    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Перевірка реверсу

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Список:")
linked_list.print_list()

linked_list.reverse()

print("\nПісля реверсу:")
linked_list.print_list()


# Перевірка сортування

print("\nСписок до сортування:")

sort_list = LinkedList()

sort_list.append(4)
sort_list.append(2)
sort_list.append(7)
sort_list.append(1)
sort_list.append(5)

sort_list.print_list()

sort_list.head = sort_list.merge_sort(sort_list.head)

print("\nПісля сортування:")

sort_list.print_list()


# Перевірка об'єднання двох відсортованих списків

print("\nОб'єднання двох списків:")

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_head = list1.sorted_merge(
    list1.head,
    list2.head
)

merged_list = LinkedList()
merged_list.head = merged_head

merged_list.print_list()