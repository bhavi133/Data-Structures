Linked List : A linked list is a linear data structure that includes a series of connected nodes. Here, each node stores the data and the address of the next node.
  
# Step 1:
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

# Step 2:
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Step 3:
    def traverse(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end="-->")
                n = n.ref
                
    # Step 4:
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Step 5:
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # Step 6:
    def insert_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in a linked list!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    # Step 7:
    def insert_before(self, data, x):
        if self.head is None:
            print("Linked list is empty!")
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not present in a linked list!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Step 8:
    def delete_from_beginning(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            self.head = self.head.ref

    # Step 9:
    def delete_from_end(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    # Step 10:
    def delete_by_value(self, x):
        if self.head is None:
            print("Linked list is empty!")
            return
        if self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node is not present in a linked list!")
            else:
                n.ref = n.ref.ref


ll1 = SinglyLinkedList()
ll1.insert_at_beginning(10)
ll1.insert_at_end(20)
ll1.insert_after(30, 10)
ll1.insert_before(40, 20)
ll1.delete_from_beginning()
ll1.delete_from_end()
ll1.delete_by_value(30)
ll1.traverse()
