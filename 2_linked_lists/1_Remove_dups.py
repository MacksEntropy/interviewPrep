# Write code to remove duplicates from a linked list. How would you solve the problem if a temporary buffer is not allowed? 
from ll_implementation import LinkedList


def removeDupes(ll):
    pass

if __name__ == "__main__":
    ll = LinkedList(["a",'b','a','d','e'])
    for node in ll:
        c_node = node
        for s_node in ll:
            if s_node.data == c_node.data:
                print("Removing ", s_node.data)
                ll.remove_node(s_node.next)
    
    print("Final ll is ", ll)