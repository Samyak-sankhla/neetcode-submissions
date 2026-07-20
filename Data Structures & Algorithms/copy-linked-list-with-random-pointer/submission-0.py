class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # Create the head of the copied list
        copy_head = Node(head.val)

        # First pass: copy all nodes using next pointers
        original_itr = head.next
        copy_itr = copy_head

        while original_itr:
            copy_itr.next = Node(original_itr.val)
            copy_itr = copy_itr.next
            original_itr = original_itr.next

        # Second pass: assign random pointers
        original_itr = head
        copy_itr = copy_head

        while original_itr:
            random_node = original_itr.random

            if random_node is None:
                copy_itr.random = None

            else:
                # Find the index of random_node in the original list
                index = 0
                search_original = head

                while search_original is not random_node:
                    search_original = search_original.next
                    index += 1

                # Go to the same index in the copied list
                search_copy = copy_head

                for _ in range(index):
                    search_copy = search_copy.next

                copy_itr.random = search_copy

            original_itr = original_itr.next
            copy_itr = copy_itr.next

        return copy_head