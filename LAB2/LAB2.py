def set_union(A, B):
    return A.union(B)

def list_union(A, B):
    result = []
    for x in A:
        if x not in B: 
            result.append(x)
    for x in B:
        result.append(x)
    return result

def set_intersection(A, B):
    return A.intersection(B)
 
def set_difference(A, B):
    return A.difference(B)

def set_isSubset(A, B):
    return A.issubset(B)

def set_ProperSubset(A, B):
    return A.issubset(B) and A != B

def Test01():
    A = {1, 2, 8}
    B = {1, 2, 3, 4, 5}
    print("Set A: ", A)
    print("Set B: ", B)
    print("Set Union: ", set_union(A, B))
    print("List Union: ", list_union(A, B))
    print("Set Intersection: ", set_intersection(A, B))
    print("Set Difference: ", set_difference(A, B))
    print("Set isSubset: ", set_isSubset(A, B))
    print("Set ProperSubset: ", set_ProperSubset(A, B))

Test01()