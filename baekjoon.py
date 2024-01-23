# # ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# # dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다.
# lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
S = list(input())
for i in range(len(S)) :
    if S[i] == "=" :
        if S[i-1] == 'c' :
            S = S.remove(S[i-1])
        elif S[i-1] == 's' :
            S = S.remove(S[i-1])
        elif S[i-1] == 'z' :
            if S[i-2] == 'd' :
                S = S.remove(S[i-2])
            else :
                S = S.remove(S[i-1])
    elif S[i] == '-' :
        if S[i-1] == 'c' :
            S = S.remove(S[i-1])
        elif S[i-1] == 'd' :
            S = S.remove(S[i-1])
    elif S[i] == 'j' :
        if S[i-1] == 'l' :
            S = S.remove(S[i-1])
        elif S[i-1] == 'n' :
            S = S.remove(S[i-1])
    else :
        pass
print(len(S))