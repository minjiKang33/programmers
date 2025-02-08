def solution(myString):
    cnt = 0
    answer = []
    for i in myString:
        if i == "x":
            answer.append(cnt)
            cnt = 0
        else :
            cnt += 1
    answer.append(cnt)
    
        
    return answer