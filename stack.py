'''
    Stack  : 
             Stack is a linear data structure which follows a particular order in which the operations are performed.
             The order may be LIFO(Last In First Out) or FILO(First In Last Out).

    We can implement stack using both Singly and Doubly Linked list's 
    In this Stack implementation ,I have used Singly Linked list 

    Basically stack has two operations push and pop

    push : this operation is used to push(Insert) data into the stack , whenever new data is pushed into the stack
            the head points to the new data

            step 1 :
                                 --------------
                        head -> | data1 | next |
                                 --------------   
            
            step 2 : When new node is pushed

                                           -------------                --------------
                        head -> new_node  | data2| next | -> prev_node | data1 | next |
                                           -------------                --------------  
    pop : this operation is used to pop(Remove) data from the stack , as stack uses LIFO (Last in First out) the data which
          is at the top is poppped out

          Suppose we have stack with three Nodes :

                --------------      --------------       --------------
               | data1 | next | -> | data2 | next | - > | data3 | next | <- head
                --------------      --------------       --------------

                In this head is pointing to Node having data value as data3 and it is at the top of the stack,
                so when popping takes place the one which entered or was pushed last will pop first
                i.e in out situation data3 will be popped then data2 and then data1
'''

#Step 1 : Initializing our Node to store data and next value
class Node:
    def __init__(self):
        self.data = None
        self.next = None

#Step 2 : Initializing Stack class
class Stack:
    def __init__(self):
        self.head = None
        self.counter = 0

    #Step 3 : Function to push elements in stack
    def push(self):
        new_node = Node()
        a = int(input("\nEnter data for the Node : "))
        new_node.data = a
        if(self.head==None):
            self.head = new_node
            new_node.next = None
            print("\n%d is pushed in stack and head is at %d" % (a,self.head.data))
            self.counter += 1
            print("\nStack has %d elements " % self.counter)
        else:
           # self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            print("\n%d is pushed in stack and head is at %d" % (a,self.head.data))
            self.counter += 1
            print("\nStack has %d elements " % self.counter)
            print("\nHead is pointing to Node : %d " % self.head.data)
        # new_node.prev = last

    # Step 4 : Function to print the stack
    def printstack(self):
        if self.head == None:
            print("\nList is empty")
        temp = self.head
        while(temp):
            print("\n")
            print(temp.data)
            temp = temp.next
    # Step 5 : Function to pop elements from stack
    def pop(self):
        temp = self.head
        print("\n%d is popped from the stack. " % self.head.data)
        self.head = temp.next
        temp = None

    # Step 6 : Function to return size of stack
    def returnelinstack(self):
        return self.counter


# Main function where all the magic will happen
if __name__ == "__main__":
    s = Stack()
    a = int(input("Enter the no of elements you want in stack "))
    for i in range(0,a):
        s.push()

    s.printstack()
    a = s.returnelinstack()
    for i in range(0,a):
        s.pop()
    s.printstack()