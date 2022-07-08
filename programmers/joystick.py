from tkinter import N


def solution(name):
    answer = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(name)
    #초기값 설정
    result = "A"*length
    answer += alphabet.find(name[0])
    result[0] = name[0]
    
    for i in range(1,length):
        if result == name:
            break
        if name[i] == "A":
            continue
        
        
    return answer