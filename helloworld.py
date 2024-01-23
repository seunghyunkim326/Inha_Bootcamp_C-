total_deungeub = []
total_hakjeom = []
number_of_subjects = 0
my_score = 0

# subject , hakjeom , deungeub = map(str,input().split())
subject = 'ObjectOrientedProgramming1'
hakjeom = '3.0'
deungeub = 'A+'
if deungeub == 'P' :
    pass
else :
    total_hakjeom.append(float(hakjeom))
    if deungeub == 'A+' :
        total_deungeub.append(4.5)
    elif deungeub == 'A0' :
        total_deungeub.append(4.0)
    elif deungeub == 'B+' :
        total_deungeub.append(3.5)
    elif deungeub == 'B0' :
        total_deungeub.append(3.0)
    elif deungeub == 'C+' :
        total_deungeub.append(2.5)
    elif deungeub == 'C0' :
        total_deungeub.append(2.0)
    elif deungeub == 'D+' :
        total_deungeub.append(1.5)
    elif deungeub == 'D0' :
        total_deungeub.append(1.0)
    elif deungeub == 'F' :
        total_deungeub.append(0)

print(total_deungeub)
print(total_hakjeom)
# print(total_deungeub, total_hakjeom)
# print(type(total_deungeub[0])) 

# for i in range(len(total_hakjeom)) :
#     number_of_subjects += total_hakjeom[i]
#     my_score += total_hakjeom[i] * total_deungeub[i]
# print(my_score/number_of_subjects)