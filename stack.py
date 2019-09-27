class Node:

    def __init__(self):
        self.data = None
        self.next = None

class stack:

    def __init__(self):
        self.head = None

    def push(self):
        a = int(input("\n Enter the data for Node :"))
        new_Node = Node()
        new_Node.data = a
        if(self.head == None):
            self.head = new_Node
            return
        else:
            new_Node.next = self.head
            self.head = new_Node
            return

    def pop(self):
        temp = self.head
        self.head = temp.next
        temp = None
        return
    
    def printstack(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    s1 = stack()
    n = int(input("Enter the no of elements you want to push into the stack :"))
    print("\nPushing elements in Stack ")
    for i in range(0,n):
        s1.push()
    print("\nPrinting the Stack ")
    s1.printstack()
    print("\nPopping the Element from Stack")
    s1.pop()
    print("\nStack after popping first element ")
    s1.printstack()