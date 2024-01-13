score = int(input())
vacation = int(input())
if vacation == 0 :
    score = 20
elif vacation != 7 :
    score -= vacation
if score < 0 :
    score = 0
print(score)
