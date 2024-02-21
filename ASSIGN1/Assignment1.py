def conjunction(p, q):
    return p and q

def disjunction(p, q):
    return p or q
    
def negation(p):
    return not p

def printTruthTable():
    print("%-8s| %-8s| %-8s| %-8s" % ("p", "q", "r", "\u00AC p ^ (q V r)"))
    print("%-8s| %-8s| %-8s| %-8s" % ("="*8, "="*8, "="*8, "="*8))
    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                print("%-8s| %-8s| %-8s| %-8s" % (p, q, r, conjunction(negation(p), disjunction(q, r))))

print("\nTruth Table for \u00AC p ^ (q V r)")
printTruthTable()