from main import measure_complexity

def test():
    code = """   
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
    """
    return measure_complexity(code)

if __name__ == '__main__':
    print(test())

