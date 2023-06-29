class Node :

    def __init__(self,data = None) :
        self.data = data
        self.next = None

class LinkList :
    def __init__(self) :
        self.head = None

    def add_from_end(self,data) :
        NewNode = Node(data)
        if not self.head : 
            self.head = NewNode
        else :
            current = self.head
            while current.next : 
                current = current.next
            current.next = NewNode
    
    def print_list(self) :
        current = self.head
        while current :
            print(current.data, end = " --> ")
            current = current.next
        print("None")
    
    def add_from_begin(self,data) :
        NewNode = Node(data)
        if not self.head :
            self.head = NewNode
        else :
            NewNode.next = self.head
            self.head = NewNode












array = LinkList()

array.add_from_end(10)
array.add_from_end(20)
array.add_from_end(4)
array.add_from_begin(0)
array.print_list()
