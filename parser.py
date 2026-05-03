import LispObj
def parse_one(lexed):
    if not lexed:
        return None
    token = lexed.pop(0)

    if token == '(':
        L = []
        while lexed and lexed[0] != ')':
            L.append(parse_one(lexed))
        if lexed:
            lexed.pop(0)
        return LispObj.LispObj(L)
    elif token == ')':
        raise SyntaxError("Unexpected )")
    else:
        return LispObj.LispObj(token)
def parse(lexed):
    all_statements = []
    while lexed:
        all_statements.append(parse_one(lexed))
    return all_statements