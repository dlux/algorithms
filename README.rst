PROBLEMS
-------

For Dynamic Connectivity Problem - Quick find and Quick Union Algorithms
~~~~~~~~~~~~~~~~


=======
Definition
=======

* Given a set of N objects.
* Union command: connect 2 objects
* Find connected query: Is there a path connecting the two objects? Do not give the path, just tell if connected.

Hint:

Connected components are sets which contains the objects that are connected. Union command create this sets or groups and find will look into each set for a given object pair.

What:

* Create union-find data structure

	* Public class UF
	* UF(int N)
	* void union(int p, int q)
        * boolean connected(int p, int q)

* Create Dynamic-connectivy client:

    * Read N numbers from input
    * Repeat:

        Read pair numbers from input

        If not yet connected, connect them and print out the pair

=======
Implementation
=======

Under src folder:

* datatype/ds_union_find.py # DataStructure
* datatype/cl_union_find.py # Client
* dynamic_connectivity/quick_find.py
* dynamic_connectivity/quick_union.py

