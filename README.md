grocery
=======
grocery is a toolkit which is collected on my daily work. 
   
Requirements
------------ 
You will need the following prerequisites in order to use grocery:
- Python 3.6+

Installation
------------
To install grocery:

.. code-block:: bash

    $ pip install grocery

Introduction
------------
list_ext which an enhancement of built-in list objects. It can filter the dict-list.
e.g.: You have the following dict-list, and want to filter the items which are 'a' > 3 and 'b' >= 4:

.. code-block:: python

    dict_of_list = [
        {'a': 1, 'b': 2},
        {'a': 4, 'b': 3},
        {'a': 3, 'b': 8},
        {'a': 6, 'b': 10},
        {'a': 2, 'b': 9}
     ]

.. code-block:: python

    from grocery.builtins_ext import list_ext
    dict_of_list = [{'a': 1, 'b': 2}, {'a': 4, 'b': 3}, {'a': 3, 'b': 8}, {'a': 6, 'b': 10}, {'a': 2, 'b': 9}]
    l = list_ext(dict_of_list)
    for item in l.filter_dict(a__gt=3, b__ge=4):
        print(item)
        
    # output: {'a': 6, 'b': 10}

Other introduction is coming