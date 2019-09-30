class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None

    def Print(self):
        # Prints list L's items in order using a loop
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()  # New line 
        
    def BuildList(self, n):
        count = 0
        temp = self.head
        while temp is not None and count <= n:
            temp.data = count
            count += 1
            temp = temp.next
        
    L = []
    L = BuildList(L, 5)
    L.Print()
    
