import LispObj
def parse(lexed: list[str]) -> list[LispObj.LispObj]:
    if not lexed:
        return None
    token = lexed.pop(0)
    if token == '(':
        L = []
        while lexed and lexed[0] != ')':
            L.append(parse(lexed))
        if lexed:
            lexed.pop(0)
        return LispObj.LispObj(L)
    elif token == ')':
        raise SyntaxError("Unexpected )")
    else:
        return LispObj.LispObj(token)

