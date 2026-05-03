import sys
import operator as op
env = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '%': op.mod,
    'abs': abs,

    '>': op.gt,
    '<': op.lt,
    '>=': op.ge,
    '<=': op.le,
    '=': op.eq,
    'not': op.not_,
    'and': lambda a, b: a and b,
    'or': lambda a, b: a or b,

    'car': lambda lst: lst[0] if isinstance(lst, list) and len(lst) > 0 else None,
    'cdr': lambda lst: lst[1:] if isinstance(lst, list) else [],
    'cons': lambda x, lst: [x] + (lst if isinstance(lst, list) else [lst]),
    'list': lambda a, b: [a, b],

    'print': lambda x: print(x) or x,
    'input': lambda msg: input(msg),
    'display': lambda x: sys.stdout.write(str(x)) or x,

    'length': len,
    'null?': lambda x: x == [],
    'type': lambda x: str(type(x)),
    'exit': lambda: sys.exit(0)
}