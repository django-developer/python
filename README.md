# example python code

Note:
each example is in its own directory containing its own README.md file .

-   binary_tree:

    code for constructing a binary tree given
    (prefix , infix) or (postfix, infix) info.

    in the case of a binary search tree,
    we just need (prefix) or (postfix) info because
    (infix) = ascending order of (prefix) or (postfix).

    also, displays the tree in the following forms:
    prefix, infix, postfix, dict of adjacency sets

-   earthquake:

    code for finding out the earthquake with maximum magnitude given the
    (address,
     distance in miles from this address,
     time duration in days going back from today
    ).

    Note:
    this code requires/depends on an external python package 'geopy'.
    you may install it on your machine using:
    sudo pip install geopy
    
