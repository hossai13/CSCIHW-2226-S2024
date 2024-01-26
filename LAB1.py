print("Hello World!")
def printName():
    print("Hello Helen!")
    
def conjunction(p, q):
    return p and q

def disjunction(p, q):
    return p or q

def exclusiveOr(p, q):
    return p != q

def conditional(p, q):
    return not p or q

def biconditional(p, q):
    if p == q:
        return True
    else:
        return False
    
def negation(p):
    return not p

# Truth Table for not p implies r.
def printTruthTable1():
    print("%-8s| %-8s| %-8s" % ("p", "r", "\u00AC p -> r"))
    print("%-8s| %-8s| %-8s" % ("="*8, "="*8, "="*8))
    for p in [True, False]:
       for r in [True, False]:
           print("%-8s| %-8s| %-8s" % (p, r, conditional(negation(p), r)))
           
# Truth Table for p or r.
def printTruthTable2():
    print("%-8s| %-8s| %-8s" % ("p", "r", "p V r"))
    print("%-8s| %-8s| %-8s" % ("="*8, "="*8, "="*8))
    for p in [True, False]:
        for r in [True, False]:
            print("%-8s| %-8s| %-8s" % (p, r, disjunction(p, r)))


def Test0():
    printName()
    a = True
    b = False
    print(conjunction(a, b))
    print(disjunction(a, b))
    print(exclusiveOr(a, b))
    print(conditional(a, b))
    print(biconditional(a, b))
    print(negation(a))
    print(negation(b))
printName()
Test0()
print("\nTruth Table for \u00AC p -> r")
printTruthTable1()
print("\nTruth Table for p V r")
printTruthTable2()