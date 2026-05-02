import LispObj
def parse(lexed: list[str]) -> list[LispObj]:
    token = lexed.pop(0)
    if token == '(':
        L = []
        while token != ')':
            L.append(parse(lexed))
        lexed.pop(0)
        return LispObj(L)
    elif token == ')':
        raise SyntaxError("Unexpected )")
    else:
        return LispObj(token)

