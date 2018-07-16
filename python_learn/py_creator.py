'''生成器'''
'''
g = (x for x in range(1,11))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''

'''杨辉三角'''
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#    1   4   6   4   1
#   / \ / \ / \ / \ / \
#  1   5   10  10  5   1
'''
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [x + L[i+1] for i,x in enumerate(L[:-1]) ] + [1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
'''
'''
def test(a):
    x = True
    while x:
        yield a
        a = a + 1
        if a >10 :
            x = False
for i in test(1):
    print(i)
'''