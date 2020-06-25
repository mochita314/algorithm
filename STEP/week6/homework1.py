'''
def foo(b):

    print('start')
    print('id(b): %#08x' % id(b))
    print('id(b[0]): %#08x' % id(b[0]))
    print('b:',b)

    b.append(2)
    print('2 appended')
    print('id(b): %#08x' % id(b))
    print('id(b[0]): %#08x' % id(b[0]))
    print('id(b[1]): %#08x' % id(b[1]))
    print('b:',b)

    b = b + [3]
    print('3 appended')
    print('id(b): %#08x' % id(b))
    print('id(b[0]): %#08x' % id(b[0]))
    print('id(b[1]): %#08x' % id(b[1]))
    print('id(b[2]): %#08x' % id(b[2]))
    print('b:',b)

    b.append(4)
    print('4 appended')
    print('id(b): %#08x' % id(b))
    print('id(b[0]): %#08x' % id(b[0]))
    print('id(b[1]): %#08x' % id(b[1]))
    print('id(b[2]): %#08x' % id(b[2]))
    print('id(b[3]]): %#08x' % id(b[3]))

    print('b:',b)

a = [1]
print('id(a): %#08x' % id(a))
print('id(a[0]): %#08x' % id(a[0]))

foo(a)
print('a:',a)
print('id(a): %#08x' % id(a))
print('id(a[0]): %#08x' % id(a[0]))
print('id(a[1]): %#08x' % id(a[1]))
'''

def foo(b):
    print('id(b): %#08x' % id(b))
    b = 1
    print('id(b): %#08x' % id(b))

a = 2
print(a)
print('id(a): %#08x' % id(a))

foo(a)
print(a)
print('id(a): %#08x' % id(a))