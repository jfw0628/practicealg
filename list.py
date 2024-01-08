class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_list_with_arr(array):
        if not array:
            return None
        head = ListNode(array[0], None)
        cursor = head
        for i in array[1:]:
            cursor.next = ListNode(i, None)
            cursor = cursor.next
    
        return head

    @staticmethod
    def print_list(head):
        array = []
        cursor = head
        while cursor:
            array.append(cursor.val)
            cursor = cursor.next
        print(array)