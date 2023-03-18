"""
-------------------------------------------------------
Binary Search Tree Visualizer Utility
Intended for the course: CP164 - Wilfrid Laurier University
Available for public use, no-copyright
-------------------------------------------------------
Author:  Benjamin Del Valle
ID:      [REDACTED]
Email:   [REDACTED]
__updated__ = "2023-03-17"
-------------------------------------------------------
"""
import math
# Known to be buggy with bigger trees

"""
****************************** TREE VISUALIZER ******************************
Takes a BST Object and represents its components as a visual tree.
Created by Benjamin Del Valle
*****************************************************************************
"""
def build_tree(bst_obj):
    """
    -------------------------------------------------------
    A public interactive method to be called to draw a BST
    as a visual tree.
    Use: print(build_tree(BST_OBJ))
    -------------------------------------------------------
    Parameters:
        bst_obj - A Binary Search Tree with elements inside (BST_linked)
    Returns:
        string - A formatted output of the visual representation of the tree
    -------------------------------------------------------
    """
    string = ""
    # 1. Ensure tree is not empty before starting
    if bst_obj._count != 0:
        lines = [] # Each entry represents a new line to be printed
        # 2. Add root to lines
        lines.append(_build_node(bst_obj._root))
        # 3. Recursive call to build rest of tree
        lines = _build_tree_auxiliary(lines, bst_obj._root, bst_obj._root._height)
        # 4. Format each element in Lines
        for i in range (0, len(lines), 1):
            string += f"{lines[i]}\n"
    return string


def _build_tree_auxiliary(llist, current_node, depth):
    """
    -------------------------------------------------------
    Recursive method which builds each individual line
    and appends it to a list of all lines within the output.
    Use: N/A [Internal Use Only]
    -------------------------------------------------------
    Parameters:
        llist - A list of all the current lines within final output (List)
        current_node - The node to reference for the current recursive call (_BST_Node)
        depth - The depth of the tree (Int)
    Returns:
        llist - A list of all lines to be utilized for final output
    -------------------------------------------------------
    """
    # Ensure we have not reached the bottom of the tree
    if current_node._left is not None or current_node._right is not None: 
        # Local Variables
        new_line = ""
        left = ""
        right = ""
        # Handling LS
        if current_node._left is not None:
            left = _build_node(current_node._left)
            depth = (depth * 3) + 1 # Optimized for ByLetter method for lab 8 CP164, this must be updated depending on the size of your values
            #new_line += f"{depth*'    '}/\n{math.floor(depth/2)*'    '}{left}"
        # Handling RS
        if current_node._right is not None:
            right = _build_node(current_node._right)
            #new_line += f"{depth*'    '}\\"
        # Combination
        new_line += f"{depth*'    '}/{math.floor(depth-1)*'    '}\\\n{math.floor((depth/2))*'    '}{left} {right}"
        #new_line += f" {left}{right}"
        llist.append(new_line)
        # Recursive calls where applicable:
        if current_node._left is not None:
            _build_tree_auxiliary(llist, current_node._left, depth=depth+1)
        if current_node._right is not None:
            _build_tree_auxiliary(llist, current_node._right, depth=depth+1)
    # Return Statement
    return llist
    # End of method

def _build_node(node_obj):
    """
    -------------------------------------------------------
    Represents a node object in string form with its
    corresponding left and right values displayed
    Use: N/A [Internal Use Only]
    -------------------------------------------------------
    Parameters:
        node_obj - A node object of an existing BST (_BST_Node)
    Returns:
        formatted_node - Formatted Node Information (String)
    -------------------------------------------------------
    """
    # 1. Represent headers in superscript format
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    left_trans = "ˡᵉᶠᵗ"
    right_trans = "ʳᶦᵍʰᵗ"
    # 2. Format Left Value
    if node_obj._left is None:
        left = "none"
    else:
        left = node_obj._left._value
    # 3. Format Right Value
    if node_obj._right is None:
        right = "none"
    else:
        right = node_obj._right._value
    # 2. Build formatted node
    formatted_node = f"[{left}{left_trans}|{node_obj._value}ʰ {str(node_obj._height).translate(SUP)}|{right_trans}{right}]"
    # Return Statement
    return formatted_node
    # End of method

# End of class
