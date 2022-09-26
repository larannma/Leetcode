
def plagiarism(A: str, B: str) -> str:
    map_A , map_B, res = {}, {}, []

    for i, a in enumerate(A):
        if a == B[i]:
            if not a in map_B:
                map_B[a] = {i}
            else:
                map_B[a].add(i)
        else:
            if not a in map_A:
                map_A[a] = {i}
            else:
                map_A[a].add(i)


    for i, b in enumerate(B):
        if b in map_B and i in map_B[b]:
            res.append("P")
            map_B[b].discard(i)
        else:
            if b in map_A and len(map_A[b]) > 0:
                res.append("S")
                map_A[b].discard(min(map_A[b]))
            else:
                res.append("I")

    print("".join(res))


A = 'CLOUD'
B = 'CUPID'

print(f'test1 = PSIIP || your1 = {plagiarism(A, B)}')

A1 = 'ALICE'
B1 = "ELIBO"

print(f'test2 = SPPII || your1 = {plagiarism(A1, B1)}')

A2 = 'ABCBCYA'
B2 = 'ZBBACAA'

print(f'test3 = IPSSPIP || your1 = {plagiarism(A2, B2)}')


a1 = 'OOPOPOO'
b1 = 'POPOOPP'

print(f'test4 = SPPPSII || your1 = {plagiarism(a1, b1)}')

a1 = 'OPPPO'
b1 = 'PPPPP'

print(f'test5 = IPPPI || your1 = {plagiarism(a1, b1)}')