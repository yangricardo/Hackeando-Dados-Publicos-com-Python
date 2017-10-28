f = open('ufrj/ufrj.txt')

funcs = {}
for linha in f:
    ids, nome, sal = linha.strip().split(',')
    funcs[ids] = [nome, float(sal)]

total = 0
for x in funcs:
    total = total + funcs[x][1]

print (total)

def s(f1): return f1[1][1]

maiores = sorted(funcs.items(), key=s, reverse=True)
for func in maiores[:50]:
    print(func)
f.close()
