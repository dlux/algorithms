'''
In order to solve Dynamic Connectivity problem.
This class represents an abstract data type for union-find.
Implementation to happen based on a given algorithm

Accept N numbers.
Accept M operations to be performed (union or find)
Operations can be intermixed (Find queries or union operand)

@author: luzC
'''


class UF:

    _n = 0
    _cc = [] # Connected componets

    def __init__(self, n):
        '''
        Constructor
        Create structure of N number of vertices/ objects
        '''
        self.initialize_objs(n)

    #########################
    # FINAL OPTIMEZED METHODS
    #########################
    def initialize_objs(self, n):
        self._n = n
        self._cc = [x for x in range(n)]

    def get_object_count(self):
        return self._n

    def get_connected_components(self):
        return self._cc

    def union(self, p_obj, q_obj):
        '''
        Connect two objects
        '''
        pass

    def connected(self, p_obj, q_obj):
        '''
        Find out if there is a conexion between 2 given objects
        '''
        return False

    def error(self, e_code=100, e_message=""):
        ecodes={
                100:'Unexpected error',
                101:'The object provided was not found',
                }
        msg = "Error {0}: {1}. {2}".format(e_code, ecodes[e_code], emessage)
        print(msg)

