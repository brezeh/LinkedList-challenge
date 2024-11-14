#assignment 4 breze howard

#Define the Node class
class Node():
    def __init__(self, value = None):
        self.value = value #store the value for the node
        self.next = None #Initialize the next pointer to None
        self.prev = None #Initialize the previous pointer to None

    #getting value of the node
    def get_value (self):
        return self.value
    
    #setting value of the node
    def set_value (self, value):
        self.value = value

    #getting next node
    def get_next (self):
        return self.next
    
    #setting next node
    def set_next (self, next):
        self.next = next

    #getting previous node
    def get_previous (self):
        return self.prev
    
    #setting previous node
    def set_previous (self, prev):
        self.prev = prev

#Define the linkedlist class
class Linkedlist():
    def __init__(self):
        self.head = None #first part of the list 
        self.tail = None #last part of the list
        self.size = 0 

    #returns the size of the list
    def count (self):
        return self.size 
    
    #adds value to the end of the list
    def add (self, value):
        new_node = Node(value) 

        if self.size == 0: #if the list is empty new node becomes both the head and tail
            self.head = self.tail = new_node
        else: #attaches to the end of the list
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node

        self.size += 1
        return self
    
    #returns the value at the given index
    def get (self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index is out of range")
        current_node = self.head
        for i in range(index):
            current_node = current_node.get_next()
            print(f"Traversing: At index {i}, node value = {current_node.get_value()}")
        return current_node
    
    #removes the given index
    def remove (self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        #case when removing head
        if index == 0:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.get_next()
                self.head.set_previous(None)
        #case when removing tail
        elif index == self.size - 1:
            self.tail = self.tail.get_previous()
            self.tail.set_next(None)
        else:
            current_node = self.head
            for i in range (index):
                current_node = current_node.get_next()
            
            #relink the previous and next nodes
            prev_node = current_node.get_previous()
            next_node = current_node.get_next()
            prev_node.set_next(next_node)
            next_node.set_previous(prev_node)

        self.size -= 1
        return self
    
    #reverse the elements in this list
    def reverse (self):
        current_node = self.head
        self.tail = current_node

        while current_node:
            #swap the next and prev pointers for each node
            current_node.set_previous(current_node.get_next())
            current_node.set_next(current_node.get_previous())
            current_node = current_node.get_previous()  # move to next node

        #swap head and tail
        self.head, self.tail = self.tail, self.head
        return self
    
    #copy the given list to this list
    def copy (self, list):
        self.clear() #clear the current list before copying
        current_node = list.head
        while current_node:
            self.add(current_node.get_value())
            current_node = current_node.get_next()
        return self
    
    #copy the given list to this list using the range from begin to end exclusive
    def copy_range (self, list, begin, end):
        self.clear()
        if begin < 0 or end > list.size or begin >= end:
            raise ValueError("Invalid range")
        current_node = list.head
        #traverse the list to the begin index
        for i in range(begin):
            current_node = current_node.get_next()
            print(f"Traversing: At index {i}, node value = {current_node.get_value()}")
        #now, copy the range from begin to end
        for i in range(begin, end):
            print(f"Copying: At index {i}, node value = {current_node.get_value()}")
            self.add(current_node.get_value())
            current_node = current_node.get_next()
        return self
    
    #return true or false if the list is empty
    def empty (self):
        return self.size == 0
    
    #return the first value in the list
    def first (self):
        return None if self.size == 0 else self.head.get_value() #if list is empty return None
    
    #return the last value in the list
    def last (self):
        return None if self.size == 0 else self.tail.get_value() #if list is empty return None
    
    #helper function to clear the list
    def clear (self):
        self.head = self.tail = None
        self.size = 0

#create a Linkedlist
ll = Linkedlist()

#add elements
ll.add(10).add(20).add(30).add(40).add(50)

#copy a range of the list (from index 1 to 3)
new_ll = Linkedlist()
print("Copying range from index 1 to 3:")
new_ll.copy_range(ll, 1, 3)

#print the copied list
current_node = new_ll.head
while current_node:
    print(current_node.get_value(), end=" ") #output should be: 20 30
    current_node = current_node.get_next()