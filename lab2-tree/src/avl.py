#!/usr/bin/env python3

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Example which shows how to override and call parent methods.  You
        may remove this function and overide something else if you'd like.
        '''
        bst.BST.add(self, v)
        
        return self.balance()

    def delete(self, v):
        """ 
        Deletes desired value then checks if there is still balance in ther tree
         """
        bst.BST.delete(self, v)

        return self.balance()

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        if self.is_empty():
            return self
        
        if (abs(self.lc().height() - self.rc().height()) >= 2):
            #Check if left is heavier/deeper/higher
            if self.lc().height() > self.rc().height():
                #case 1 or 2
                if self.lc().lc().height() >= self.lc().rc().height():
                    #case 1 srr()
                    return self.srr()
                else:
                    #case 2 drr()
                    return self.drr()

            #right is heavier/deeper/higher
            else:
                #case 3 or 4
                
                if self.rc().lc().height() > self.rc().rc().height():
                    #case3 dlr()
                    return self.dlr()
                else:
                    #case 4 slr()
                    return self.slr()

        
        return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        node = self.rc()
        self.set_rc(node.lc())
        node.set_lc(self)
        return node

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        node = self.lc()
        self.set_lc(node.rc())
        node.set_rc(self)
        return node

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        self.set_rc(self.rc().srr())
        return self.slr()
        

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        self.set_lc(self.lc().slr())
        return self.srr()
        

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
