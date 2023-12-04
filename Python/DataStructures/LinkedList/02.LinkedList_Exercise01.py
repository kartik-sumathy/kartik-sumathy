# class fruitList:
#     def __init__(self,fruit=None):
#         self.fruit = fruit


#     def printFruit(self):
#         fruit = self.fruit
#         return fruit

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class linkedNode:
    def __init__(self):
        self.head = None

    def insert_values(self,datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)

    def print(self):
        if self.head is None:
            print('LinkedList is None')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' > ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)



fl =linkedNode()

fl.insert_values(["banana","mango","grapes","orange"])

fl.print()




""" fl = fruitList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print() """

