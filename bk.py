N = int(input())
count = 0
L = []
for _ in range(N) :
    S = str(input())
    count += 1
    for i in range(len(S)) :
        if S.count(S[i]) >1 :
            for j in range(len(S)) :
                if S[i] == S[-j] :
                    count -= 1
                    break
                else :
                    pass
        else :
            pass
print(count)