def solution(balls, share):
    answer = 1
    m = 1
    for i in range(share):
        answer *= balls - i
    for i in range(share):
        m *= share - i
    return answer / m