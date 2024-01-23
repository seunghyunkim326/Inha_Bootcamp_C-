S = str(input())
while 'c=' in S or 'c-' in S or 'dz=' in S or 'd-' in S or 'lj' in S or 'nj' in S or 's=' in S or 'z=' in S :
    if 'dz=' in S :
        S = S.replace('dz=' , '1')
    elif 'z=' in S :
        S = S.replace('z=' , '2')
    if 'c=' in S :
        S = S.replace('c=' , '*')
    if 'c-' in S :
        S = S.replace('c-' , '*')
    if 'd-' in S :
        S = S.replace('d-' , '*')
    if 'lj' in S :
        S = S.replace('lj' , '*')
    if 'nj' in S :
        S = S.replace('nj' , '*')
    if 's=' in S :
        S = S.replace('s=' , '*')
print(len(S))