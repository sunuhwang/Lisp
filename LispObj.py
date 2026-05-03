from fractions import Fraction
class LispObj:
    def __init__(self,Value):
        self.Value = Value
    def eval(self,env):
        if type(self.Value) != list:
             if self.Value.startswith('"') and self.Value.endswith('"'):
                return self.Value[1:-1]
             elif self.Value == '#t':
                return True
             elif self.Value == '#f':
                return False
             elif type(self.Value) == str and  not self.Value.startswith('"') and not self.Value.endswith('"') and not self.Value[0].isdigit():
                return env[self.Value]
             else:
                if '/' in self.Value:
                    return Fraction(self.Value)
                else:
                    return self.Value.replace('#','0') if self.Value[2:3] == '#' else float(self.Value)
        else:
            match self.Value[0].Value:
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
                    if type(self.Value[1].Value) == list:
                        env[self.Value[1].Value[0].Value] = [self.Value[1].Value[1:],self.Value[2]]
                    else:
                        env[self.Value[1].Value] = self.Value[2].eval(env)
                case _:
                    args = [i.eval(env) for i in self.Value[1:]]
                    fn = self.Value[0].eval(env)
                    if callable(fn):
                        return fn(*args)
                    else:
                        local_env = env.copy()
                        body = fn[1]
                        params = fn[0]
                        for p, a in zip(params, args):
                            p_name = p.Value if hasattr(p, 'Value') else p
                            local_env[p_name] = a
                        return (body if type(body) == LispObj else LispObj(body)).eval(local_env)