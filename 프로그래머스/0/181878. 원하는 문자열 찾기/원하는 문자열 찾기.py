def solution(myString, pat):
    answer = 0
    myString = myString.lower()
    pat = pat.lower()
    
    for i in range(len(myString) - len(pat) + 1):
        if myString[i] == pat[0]:
            for j in range(len(pat)):
                if myString[i+j] != pat[j]:
                    break
                elif j == len(pat) - 1:
                    answer = 1

    return answer