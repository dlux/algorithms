'''
In order to solve Dynamic Connectivity problem.
This class represents an implemtation of abstract data type union-find.
Implementation is of quick_union algorithm - Lazy approach

Accept N numbers.
Accept M operations to be performed (union or find)
Operations can be intermixed (Find queries or union operand)

@author: luzC
'''
from datatypes.ds_union_find import UF


class QUICK_UNION(UF):

    def union(self, p_obj, q_obj):
        '''
        Connect two objects
        '''
        root_p = self.find_root(p_obj)
        root_q = self.find_root(q_obj)

        self._cc[root_p] = self._cc[root_q]

        print(self._cc)

    def connected(self, p_obj, q_obj):
        '''
        Find out if there is a conexion between 2 given objects
        '''
        return self.find_root(p_obj) == self.find_root(q_obj)

    def find_root(self, obj):
        '''
        Find root
        '''
        if obj not in range(self._n):
            self.error(101, str(obj))
            exit(1)

        # With a while loop
        while(obj != self._cc[obj]):
            obj = self._cc[obj]
        return obj

        # Use recursive method instead of while loop
        #root = self._cc[obj]
        #return root if root == obj else self.find_root(root)

class QUICK_UNION_OPTIMIZED(QUICK_UNION):
    '''
    Optimized by keeping track of tree weight
    '''
    def __init__(self, n):
        super(QUICK_UNION_OPTIMIZED, self).__init__(n)
        self._cc_size = [1]*n

    def union(self, p_obj, q_obj):
        '''
        Connect two objects
        Use the weight of the object trees.
        Place the smaller tree under the larger tree to avoid larger trees
        Need to keep track of tree size
        '''
        root_p = self.find_root(p_obj)
        root_q = self.find_root(q_obj)

        p_size = self._cc_size[root_p]
        q_size = self._cc_size[root_q]

        if p_size < q_size:
            self._cc[root_p] = self._cc[root_q]
            self._cc_size[root_q] += p_size
        else:
            self._cc[root_q] = self._cc[root_p]
            self._cc_size[root_p] += q_size

        print(self._cc)

class QUICK_UNION_OPTIMIZED_PATH_COMPRESSION(QUICK_UNION_OPTIMIZED):
    '''
    Optimized by keeping track of tree weight
    And flattening the tree with path compression
    After finding the root of X, move X under its parent root directly.
    Also move parents of X directly under parent root.
    '''
    def find_root(self, obj):
        '''
        Find root and flatten tree
        '''
        if obj not in range(self._n):
            self.error(101, str(obj))
            exit(1)

        # With a while loop
        while(obj != self._cc[obj]):
            # make grandparent the root
            # other way is to add a second loop to set to root all examined
            #nodes in order to flaten the tree
            self._cc[obj] = self._cc[self._cc[obj]]
            obj = self._cc[obj]
        return obj

