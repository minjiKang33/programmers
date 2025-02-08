def solution(arr, query):
    cnt = 0
    for i in query:
        if cnt % 2 == 0:
            del arr[i+1:]
        else:
            del arr[:i]
        cnt += 1
    return arr