from tkinter import N


def solution(name):
    answer = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(name)
    #초기값 설정
    result = "A"*length
    #answer += alphabet.find(name[0])
    #result[0] = name[0]
    
    for i in range(length):
        if i == 0 and name[1:-1] == "A"*(length-2):
            answer += 1
            
        if result == name:
            break
        if name[i] == "A":
            continue
        answer += alphabet.find(name[i])
        result[i] = name[i]
        
        
    return answer