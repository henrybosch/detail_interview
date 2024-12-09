import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Tree, Node
from typing import Generator

PY_LANGUAGE = Language(tspython.language())

def traverse_tree(tree: Tree) -> Generator[Node, None, None]:
    cursor = tree.walk()

    visited_children = False
    while True:
        if not visited_children:
            yield cursor.node
            if not cursor.goto_first_child():
                visited_children = True
        elif cursor.goto_next_sibling():
            visited_children = False
        elif not cursor.goto_parent():
            break

def measure_complexity(code: str) -> int:

    parser = Parser(PY_LANGUAGE)

    tree = parser.parse(bytes(code,"utf8"))

    count = 0
    for n in traverse_tree(tree):
        if n.type in ['if','while','for']:
            count += 1
    return count