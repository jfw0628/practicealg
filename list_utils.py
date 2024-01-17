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
        

class List:
    def __init__(self, head):
        self.head = head

    @classmethod
    def create_list_with_arr(cls, array):
        if not array:
            return None
        
        a_list = cls(ListNode(array[0], None))
        cursor = a_list.head
        for i in array[1:]:
            cursor.next = ListNode(i, None)
            cursor = cursor.next
    
        return a_list
    
    def to_python_list(self):
        array = []
        cursor = self.head
        while cursor:
            array.append(cursor.val)
            cursor = cursor.next
        return array

    def print_list(self):
        print(self.to_python_list())
        
    
    def __eq__(self, other):
        if not other or (not other.head and self.head) or (not self.head and other.head):
            return False
        
        if not other.head and not self.head:
            return True
        
        cursor_curr = self.head
        cursor_other = other.head
        
        while cursor_curr and cursor_other:
            if cursor_curr.val != cursor_other.val:
                return False
            else:
                cursor_curr = cursor_curr.next
                cursor_other = cursor_other.next
        
        if cursor_curr != cursor_other:
            return False
        
        return True
        
        
        
        
        
        
    
    
        
   