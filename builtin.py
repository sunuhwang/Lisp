import operator as op
import sys
from fractions import Fraction

env = {
    ('+', 'a', 'b'): lambda a, b: a + b,
    ('-', 'a', 'b'): lambda a, b: a - b,
    ('*', 'a', 'b'): lambda a, b: a * b,
    ('/', 'a', 'b'): lambda a, b: a / b,
    ('%', 'a', 'b'): op.mod,
    ('abs', 'x'): abs,

    ('>', 'a', 'b'): op.gt,
    ('<', 'a', 'b'): op.lt,
    ('>=', 'a', 'b'): op.ge,
    ('<=', 'a', 'b'): op.le,
    ('=', 'a', 'b'): op.eq,
    ('not', 'x'): op.not_,
    ('and', 'a', 'b'): lambda a, b: a and b,
    ('or', 'a', 'b'): lambda a, b: a or b,

    ('car', 'lst'): lambda lst: lst[0] if isinstance(lst, list) and len(lst) > 0 else None,
    ('cdr', 'lst'): lambda lst: lst[1:] if isinstance(lst, list) else [],
    ('cons', 'x', 'lst'): lambda x, lst: [x] + (lst if isinstance(lst, list) else [lst]),
    ('list', 'a', 'b'): lambda a, b: [a, b],

    ('print', 'x'): lambda x: print(x) or x,
    ('input', 'msg'): lambda msg: input(msg),
    ('display', 'x'): lambda x: sys.stdout.write(str(x)) or x,

    ('length', 'lst'): len,
    ('null?', 'x'): lambda x: x == [],
    ('type', 'x'): lambda x: str(type(x)),
    ('exit',): lambda: sys.exit(0)
}
