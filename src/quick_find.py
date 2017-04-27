'''
In order to solve Dynamic Connectivity problem.
This class represents an implemtation of abstract data type union-find.
Implementation is of quick_find algorithm

Accept N numbers.
Accept M operations to be performed (union or find)
Operations can be intermixed (Find queries or union operand)

@author: luzC
'''
from datatypes.ds_union_find import UF


class QUICK_FIND(UF):

    def union(self, p_obj, q_obj):
        '''
        Connect two objects
        '''
        if self.connected(p_obj, q_obj):
            return

        to_replace = self._cc[p_obj]
        replace_with = self._cc[q_obj]
        for x in range(self._n):
            if self._cc[x] == to_replace:
                self._cc[x] = replace_with

        print("Changed {0}, {1}".format(p_obj, q_obj))

    def connected(self, p_obj, q_obj):
        '''
        Find out if there is a conexion between 2 given objects
        '''
        if p_obj not in range(self._n) or q_obj not in range(self._n):
            error(101)

        return True if self._cc[p_obj] == self._cc[q_obj] else False

    def find(self, p_obj, q_obj):
        connected(p_obj, q_obj)

# Analysis:
# initialization: O(n)
# union: O(n)
# connected|find: O(1)

# Hence O(n^2)
# Explained on https://justin.abrah.ms/computer-science/big-o-notation-explained.html
