def solution(arr):
    arr2 = arr
    answer = 0
    
    while  True :
        arr = arr2
        arr2 = []
        for i in arr:
            if (i >= 50) and (i % 2 == 0):
                arr2.append(i / 2)
            elif (i < 50) and (i % 2 == 1):
                arr2.append(i * 2 + 1)
            else :
                arr2.append(i)
    
        if arr == arr2 : break
        answer += 1
        
    return answer