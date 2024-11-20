"""
This is a sample module for developing/testing codetags
"""

# NOTE: 'note' out of functions, module1, line 5, no closing brackets

# NOTE: 'note' multirow, out of functions, module1, line 7, no closing brackets
# 'note' multirow, out of functions, module1, line 8, no closing brackets

# TODO: 'todo' out of functions, module1, line 10, with closing brackets <>

class Aclass():

    # BUG: 'bug' in class, module1, line 14, brackets date 2022-01-01, multirow
    # 'bug' in class, module1, line 14, brackets date 2022-01-01, multirow <d:2022-01-01>

    def __init__(self, arg1: str='test'):
        """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. In bibendum
        nisl vitae dolor maximus volutpat. In ac est faucibus, pulvinar neque
        ultricies, mattis neque.

        Parameter
        ---------
        arg1 : str
        """
        # TODO: 'todo' in method, module1, line 26, no closing brackets
        self.arg1 = arg1


def a_function() -> None:
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. In
    bibendum nisl vitae dolor maximus volutpat. In ac est faucibus,
    pulvinar neque ultricies, mattis neque.
    """
    # normal coment, do not include
    a_object = Aclass() # FIXME: 'fixme' in function, module1, line 36, no brackets

    return a_object


def another_function() -> None:
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. In bibendum
    nisl vitae dolor maximus volutpat. In ac est faucibus, pulvinar neque
    ultricies, mattis neque.
    """

    a_object = Aclass() # TODO: 'todo' in function, module1, line 47, brackets p2, multiline
    # 'todo' in function, module1, line 47, brackets p2, multiline <p:2>

    # normal coment, do not include
    return a_object


def main() -> None:
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. In bibendum
    nisl vitae dolor maximus volutpat. In ac est faucibus, pulvinar neque
    ultricies, mattis neque.
    """

    # FIXME: 'fixme' in function 'main', module1, line 60, with brackets p1 <p:1>
    a_function() # normal coment, do not include


if __name__ == "__main__":
    main()
