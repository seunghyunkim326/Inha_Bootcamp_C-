S = str(input())
L = [0]*26
S = S.upper()
for i in range(65,91) :
    for j in range(len(S)) :
        if S[j] == chr(i) :
            L[i%65] += 1
if L.count(max(L)) == 1 :
    print(chr(65+L.index(max(L))))
else :
    print('?')