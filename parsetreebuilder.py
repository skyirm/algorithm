from numbers import Number
import operator
from stack import Stack
from binarytree import Binarytree


def build_parse_tree(exp: str) -> Binarytree:
    fplist = exp.split()
    pstack = Stack()
    ptree = Binarytree('')
    pstack.push(ptree)
    current_tree = ptree
    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            pstack.push(current_tree)
            current_tree = current_tree.get_left_child()
            
        elif i not in "+-*/)":
            current_tree.set_root_val(eval(i))
            parent = pstack.pop()
            current_tree = parent
        elif i in "+-*/":
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            pstack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = pstack.pop()
        else:
            raise ValueError("Unknown operator" + i)
    return ptree


def evaluate(parse_tree: Binarytree) -> Number:
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}

    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.get_root_val()

if __name__ == "__main__":
    ptree = build_parse_tree(input(":"))
    print(evaluate(ptree))
    