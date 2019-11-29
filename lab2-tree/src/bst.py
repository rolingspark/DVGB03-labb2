#!/usr/bin/env python3

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.is_empty():
            return False
        
        if v == self.value():
            return True
        elif v < self.value():
            return self.lc().is_member(v)
        elif v > self.value():
            return self.rc().is_member(v)

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        return 1 + self.lc().size() + self.rc().size()
            

    def height(self):
        '''
        Returns the height of the tree.
        '''
        if self.is_empty():
            return 0
        
        else:
            #Find the height of left and right subtree
            l_height = self.lc().height()
            r_height = self.rc().height()

            #return whichever is the biggest
            if (l_height > r_height):
                return l_height + 1
            else:
                return r_height + 1

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return[]

        return (self.lc().inorder() + [self.value()] + self.rc().inorder())

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return (self.lc().inorder() + self.rc().inorder() + [self.value()])

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        
        if self.is_empty():
            return []
        
        temp_queue = []
        arr = []
        temp_queue.append(self)
 
        while(len(temp_queue) > 0):
            
            arr.append(temp_queue[0]._value),
            parent = temp_queue.pop(0)
            
            if parent._left_child is not None:
                temp_queue.append(parent.lc())
            
            if parent._right_child is not None:
                temp_queue.append(parent.rc())
            
        counter = 0
        for i in range(0, self.height()):
            for j in range(0, 2*i):
                if arr[counter] == None:
                    arr.insert((counter*2)+1, None)
                    arr.insert((counter*2)+2, None)
                counter += 1
        while(len(arr) > (2**self.height()-1)):
            arr.pop()

        return arr


    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self
    
    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        log.info("TODO@src/bst.py: implement delete()")
        return self

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
