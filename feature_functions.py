def f0(w):
    return {'last-letter': w[-1]}

def f1(w):
    return {'last-2-letters': w[-2:]}

def f2(w):
    return {'last-3-letters': w[-3:]}

def f3(w):
    return {'first-letter': w[0]}

def f4(w):
    return {'first-2-letters': w[:2]}

def f5(w):
    return {'first-3-letters': w[:3]}

def f6(w):
    return {'v-count': sum(w.count(l) for l in 'aeiou')}

def f7(w):
    return {'c-count': sum(w.count(l) for l in 'qwrtyplkjhgfdszxcvbnm')}

def f8(w):
    return {'len': len(w)}

def f9(w):
    r = {}
    for l in "abcdefghijklmnopqrstuvwxyz":
        r['has %s' % l] = (l in w.lower())
    return r

def f10(w):
    r = {}
    for l in "abcdefghijklmnopqrstuvwxyz":
        r['count %s' % l] = w.lower().count(l)
    return r

def f11(w):
  return {'a-count': w.count('a')}

def f12(w):
  return {'b-count': w.count('b')}

def f13(w):
  return {'c-count': w.count('c')}

def f14(w):
  return {'d-count': w.count('d')}

def f15(w):
  return {'e-count': w.count('e')}

def f16(w):
  return {'f-count': w.count('f')}

def f17(w):
  return {'g-count': w.count('g')}

def f18(w):
  return {'h-count': w.count('h')}

def f19(w):
  return {'i-count': w.count('i')}

def f20(w):
  return {'j-count': w.count('j')}

def f21(w):
  return {'k-count': w.count('k')}

def f22(w):
  return {'l-count': w.count('l')}

def f23(w):
  return {'m-count': w.count('m')}

def f24(w):
  return {'n-count': w.count('n')}

def f25(w):
  return {'o-count': w.count('o')}

def f26(w):
  return {'p-count': w.count('p')}

def f27(w):
  return {'q-count': w.count('q')}

def f28(w):
  return {'r-count': w.count('r')}

def f29(w):
  return {'s-count': w.count('s')}

def f30(w):
  return {'t-count': w.count('t')}

def f31(w):
  return {'u-count': w.count('u')}

def f32(w):
  return {'v-count': w.count('v')}

def f33(w):
  return {'w-count': w.count('w')}

def f34(w):
  return {'x-count': w.count('x')}

def f35(w):
  return {'y-count': w.count('y')}

def f36(w):
  return {'z-count': w.count('z')}

def f37(w):
    return {'has-a': 'a' in w}

def f38(w):
    return {'has-b': 'b' in w}

def f39(w):
    return {'has-c': 'c' in w}

def f40(w):
    return {'has-d': 'd' in w}

def f41(w):
    return {'has-e': 'e' in w}

def f42(w):
    return {'has-f': 'f' in w}

def f43(w):
    return {'has-g': 'g' in w}

def f44(w):
    return {'has-h': 'h' in w}

def f45(w):
    return {'has-i': 'i' in w}

def f46(w):
    return {'has-j': 'j' in w}

def f47(w):
    return {'has-k': 'k' in w}

def f48(w):
    return {'has-l': 'l' in w}

def f49(w):
    return {'has-m': 'm' in w}

def f50(w):
    return {'has-n': 'n' in w}

def f51(w):
    return {'has-o': 'o' in w}

def f52(w):
    return {'has-p': 'p' in w}

def f53(w):
    return {'has-q': 'q' in w}

def f54(w):
    return {'has-r': 'r' in w}

def f55(w):
    return {'has-s': 's' in w}

def f56(w):
    return {'has-t': 't' in w}

def f57(w):
    return {'has-u': 'u' in w}

def f58(w):
    return {'has-v': 'v' in w}

def f59(w):
    return {'has-w': 'w' in w}

def f60(w):
    return {'has-x': 'x' in w}

def f61(w):
    return {'has-y': 'y' in w}

def f62(w):
    return {'has-z': 'z' in w}
