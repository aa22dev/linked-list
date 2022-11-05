class Node: # Node Class for LinkedList
    def __init__(self, data=None): # constructor for node accepting data
        self.element = data # set user inputted data
        self.next = None # add ref of next node


class LinkedList: 
    def __init__(self): # constructor to initialize linked list with first node
        self.head = Node() # creating head for linkedlist
        self.__counter = 0 # counter to keep record of total no. of nodes attached with linkedlist

    def append(self, data): # function to append new node to linkedlist
        if self.head.element is None: # check whether the head of linkedlist contain any data or not
            self.head.element = data # put data in head of linked list if it doesn't already contain any data
        else:
            n = Node(data) # create new node
            current = self.head # temporary variable to store address of head node of linkedlist
            while current.next is not None: # loop until last node (condition states that if the next element of current node doesn't refrence to any new node then stop)
                current = current.next # store address of next node
            current.next = n # when current pointer have the address of last node then set it's next element with the address of new node
        self.__counter = self.__counter + 1 # increment counter as new node is added

    def appendleft(self, data): # function to append new child on the left of linked list
        if self.head.element is None: # check whether the head of linkedlist contain any data or not
            self.head.element = data # put data in head of linked list if it doesn't already contain any data
        else:
            n = Node(data) # create new node
            current = self.head # temporary variable to store address of head node of linkedlist
            self.head = n # store address of new node in head to make it a new head node of linkedlist
            n.next = current # store the address of current head node in the new node to make it a next node after new node
        self.__counter = self.__counter + 1 # increment counter

    def len(self): # returns total no. of nodes of linkedlist
        return self.__counter

    def insert(self, data, index): # function to insert new node at any position
        if index < self.len(): # if the position passed by user is less than total length of linkedlist
            if index == 0: # then check if it is equal to zero
                self.appendleft(data) # insert on left of linked list
            else:
                current = self.head # temporary variable to store address of head node
                for i in range(0, index - 1): # loop until the node before the position specified by user is reached
                    current = current.next # store reference of next node in current variable
                n = Node(data) # create new node
                n.next = current.next # store address of node already at the position specified by user in new node next element
                current.next = n # store address of new node in next element
                self.__counter = self.__counter + 1 # increment counter

        elif index == self.len(): # if position specified is the last index
            self.append(data) # append at the end of linkedlist

        else:
            print("Index doesn't exist") # print invalid index

    def pop(self):
        if self.head.element is None: # if head is not defined
            r = "Linked List is Empty!" # print empty linked list
        else:
            current = self.head # set address of head in temporary var
            while current.next.next is not None: # if next of next node doesn't exist stop the loop
                current = current.next # store address of next node
            r = current.next.element # store data of next element in temp var
            current.next.element = None # set it to none
            current.next = None 
            self.__counter = self.__counter - 1 # decrement the counter
        return r # return value

    def popleft(self):
        if self.head.element is None: # if head is not defined
            r = "Linked List is Empty!" # print empty linked list
        else:
            current = self.head # set address of head in temporary var
            r = current.element # set data of head in temporary var
            self.head = current.next # store next node in head
            current.element = None # set old node to null
            current.next = None
            self.__counter = self.__counter - 1 # decrement the counter
        return r

    def display(self): # function to print list
        current = self.head # store address of head node in temp var
        r = [current.element] # store value of head in temp var
        while current.next is not None: # loop until last node is reached
            current = current.next # store address of next node in temp var
            r.append(current.element) # append it's data to temp list
        return f"LinkedList({r})" # return linkedlist data


if __name__ == "__main__":
    linked_list = LinkedList()  # initializing LinkedList class object
    linked_list.append(2)  # Adding data on the end of the linked list
    linked_list.append(3)
    linked_list.append(8)
    linked_list.append(9)
    print(f"Data added on the end: {linked_list.display()}\n")  # LinkedList([2, 3, 8, 9])

    linked_list.appendleft(10)
    linked_list.appendleft(12)
    print(f"Data added on the front: {linked_list.display()}\n")  # LinkedList([12, 10, 2, 3, 8, 9])

    print(linked_list.pop())  # 9
    print(linked_list.pop())  # 8
    print(linked_list.popleft())  # 12

    print(f"\nData after popping: {linked_list.display()}\n")  # LinkedList([10, 2, 3])

    linked_list.insert(10, 4)  # Error: Index doesn't exist
    linked_list.insert(14, 3)  # perform functionality of appendleft() function as 3 is the last index
    linked_list.insert(16, 2)  # Value will be added at index = 2

    print(f"\nData after insertion: {linked_list.display()}\n")  # LinkedList([10, 2, 16, 3, 14])

    print(f"Length of Linked List: {linked_list.len()}")  # 5
