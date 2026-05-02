import re
def lex(code: str) -> list[str]:
    #delete comment
    code = re.sub(r";.*", "", code)
    #lexing
    tokens = re.findall(
        r"""
            ".*?"|                                               
            [+-]?(?:\#x[0-9a-fA-F]+|\#b[01]+|\#o[0-7]+|(?:\d+\.?\d*|\.\d+)(?:[sSfFdDlL][+-]?\d+)?(?:/\d+)?)| 
            \#t|\#f|                                             
            [()]|                                                
            [^\s()]+                                             
            """,
        code,re.X)
    return tokens