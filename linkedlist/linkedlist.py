"""
 1. Linked is a linear data structure.
 2. Made chain of nodes.
 3. Node - Element of LinkedList.
 4. Each node contains data and link of the next node.
 5. Last node stores data and reference to empty value or Null.
 6. Reference(link) of node `n` is stored in node `n-1`.
 7. First node is called head/front.
 8. First node is called tail/end.
 9. Dynamic data structure: Size need not to be mentioned.
 10. Node/elements are stored randomly in memory.
 11. We don't need Contagious Memory Location - allocating consecutive memory blocks.
 12. Advantage: - Uses Dyanmic memory location.
                - Insertion and Deletion is easier.
                - Can be used to implement Stack, Graph, Queue.
                - Represent and manipulate polynomials.
 13. Disadvantage: - Needs extra memory
                   - Randomly accessing elements is not possible.
                    (Since each nodes know the reference of the next node)
"""

# Types of Linked List
"""
 1. Singly Linked List
 2. Doubly Linked List
 3. Circular Linked List
"""

# SINGLY LINKED LIST
"""
  - If each nodes contain only one link i.e link of the next node.
  - Every node contains data and link/reference to the next node.
  - Last node contains referenc to Null/empty value.
  - First node is Head
  - Allows you to move in forward direction.
  - Backward direction movement is not easier.
  - Operations: Adding elements, Removing elements, Traversing LinkedList
        
        ADD
  * To add we need to break the already existing link.
  * We can add at the beginning, at the end, and in between the nodes.

  `At the Beginning LL` 
  i.   Create a new node. (with some data, and it points to NULL)
  ii.  Point it to the first node i.e add reference of the first node to the new node i.e HEAD(Head contains ref to the first node).
       (Initially the reference is NULL) 
  iii. Point the HEAD to the new node.

  `At the End of LL`
  i.   Create a new node. (with some data, and it points to NULL)
  11.  Move to the last node.
  iii. Change the link from NULL to the reference(address) of the new node.

  `In between Nodes`
  i.   Create a new node. (with some data, and it points to NULL)
  ii.  Move to the node after which you want to add the new node.
  iii. Change it's reference to the address of the new node.
  iv.  Now, Change the reference of new node from NULL to the reference of the node which will be next to it.
       
        DELETE
  `FIRST`
  Change the HEAD's Link to the second node.

  `LAST`
  Go to the second last element, and make it's reference(pointer/link) as NULL

  `In BETWEEN`
   - Go to the element before the element to be deleted.
   - Change it's link to the reference of the element which is next to the element that is to be deleted.

   `TRAVERSE`
   - Check if LinkedList is empty.
   - If not, go through each node 
"""


class Node:
    # Create individual nodes
    def __init__(self, data):
        self.data = data
        self.ref = None  # We are creating independent nodes, hence the reference is None


class LinkedList:
    def __init__(self):
        self.head = None


    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None: # Until we've reached the last element
                print(n.data,"--->",end=" ")    
                n = n.ref        # reference changes to the next node
    

    def add_begin(self, data):
        new_node = Node(data)    # Creating a New Node
        new_node.ref = self.head # pointing to the HEAD as the ref of first element is stored in HEAD
        self.head = new_node     # Pointing the head to the newly created node (which is at the beginning) 


    def add_end(self, data):
        new_node = Node(data)

        # Check if LinkedList is empty
        if self.head is None:
            # We have to create first Node
            self.head = new_node # store ref of new node in HEAD
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
 


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(63)
LL1.add_begin(91)
LL1.add_end(101)
LL1.add_end(56)



LL1.print_LL()
