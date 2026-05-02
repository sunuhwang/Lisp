from fractions import Fraction
class LispObj:
    def __init__(self,Value):
        self.Value = Value
    def eval(self,env):
        if type(self.Value) != list:
            if type(self.Value) == str and  not self.Value.startswith('"') and not self.Value.endswith('"'):
                return env[self.Value]
            elif type(self.Value) == str:
                return self.Value[1:-1]
            elif self.Value == '#t':
                return True
            elif self.Value == '#f':
                return False
            else:
                if '/' in self.Value:
                    return Fraction(self.Value)
                else:
                    return self.Value.replace('#','0') if self.Value[2] == '#' else float(self.Value)
        else:
            match self.Value[0]:
                case 'if':
                    _, test, conseq, alt = self.Value
                    exp = conseq if LispObj(test).eval(env) else alt
                    return LispObj(exp).eval(env)
                case 'cond':
                    before_cond = False
                    for i in range(len(self.Value[1:])):
                        if not before_cond and self.Value[1][i + 1]:
                            return self.Value[1][i + 1].eval(env)
                        else:
                            before_cond = self.Value[1][i + 1]
                case 'quote':
                    return self.Value[1]
                case 'define':
                    if type(self.Value[1]) == list:
                        env[tuple(self.Value[1])]  = self.Value[2]
                    else:
                        env[self.Value[1]] = self.Value[2]
                case _:
                    local_env = {}
                    for args in self.Value[1:]:
                        for functions in env.keys():
                            if functions[0] == self.Value[0]:
                                for name, val in zip(functions[1:], args):
                                    local_env[name] = LispObj(val).eval(env)
                                if callable(env[functions[0]]):
                                    return env[functions](*local_env.values())
                                else:
                                     return LispObj(env[functions]).eval(local_env)
                    raise NameError("Unknown function")
