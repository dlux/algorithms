ABOUT THIS PROJECT
-------------------

This repository contains a series of algorithm implementations.
You can run them all from defined cli:

.. code-block:: bash

    dlux_alg union-find 
    
For all algorithms or details of the input for an algorithm:

.. code-block:: bash

    dlux_alg
    dlux_alg --help
    dlux_alg union-find  --help

Run the clients directly from src/cmd:

.. code-block:: bash

    python3 client_union_find.py


**INSTALLATION**

Clone the repository

.. code-block:: bash

  $ git clone https://github.com/dlux/algorithms.git 

Install package from src or use Vagrant VM

.. code-block:: bash

  $ pushd algorithms
  $ pip install -e ./

  # OR

  $ pushd algorithms
  $ vagrant up;
  $ vagrant ssh
  
  # To verify installation:
  $ pip list | grep dluxAlgorithms


Package Structure

.. code-block:: bash

    dluxAlgorithms
    ├── 
    ├── LICENSE
    ├── README.rst
    ├── requirements.txt
    ├── setup.py
    ├── src
    │   ├── binary_search.py
    │   ├── cmd
    │   │   ├── client_template.py
    │   │   ├── main.py
    │   │   ├── client_three_sum.py
    │   │   └── client_union_find.py
    │   ├── common.py
    │   ├── datatypes
    │   │   ├── ds_union_find.py
    │   ├── quick_find.py
    │   ├── quick_union.py
    │   └── three_sum.py
    └── tests

PROBLEMS AND ALGORITHMS
~~~~~~~~~~~~~~~~~~~~~~~

For Dynamic Connectivity Problem - Quick find and Quick Union Algorithms
~~~~~~~~~~~~~~~~

**Definition**

* Given a set of N objects.
* Union command: connect 2 objects
* Find connected query: Is there a path connecting the two objects? Do not give the path, just tell if connected.

**Hint:**

Connected components are sets which contains the objects that are connected. Union command create this sets or groups and find will look into each set for a given object pair.

**What:**

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

* Using quick find algorithm

* Using quick union algorithm

**Implementation Files**

Under src folder:

* datatype/ds_union_find.py # DataStructure
* client_union_find.py     # Client for quick_find and quick_union
* quick_find.py            # Actual algorithm implementation
* quick_union.py           # Actual algorithm implementation

Three Sum Algorithm
~~~~~~~~~~~~~~~~~~~

**Definition**

* Given a set of N objects.

**Hint:**


**What:**


**Implementation Files**

Under src folder:

* client_three_sum.py      # Client consuming implementation(s)
* three_sum.py           # Actual algorithm implementation(s)

Binary Search Algorithm
~~~~~~~~~~~~~~~~~~~

**Definition**

* Given a set of N objects.

**Hint:**


**What:**


**Implementation Files**

Under src folder:

* client_searches.py     # Client consuming implementation(s)
* binary_search.py           # Actual algorithm implementation(s)

<ALGORITHM or PROBLEM NAME
~~~~~~~~~~~~~~~~~~~

**Definition**


**Hint:**


**What:**


**Implementation Files**

Under src folder:

* client_<name>.py      # Client consuming implementation(s)
* <name>.py           # Actual algorithm implementation(s)

