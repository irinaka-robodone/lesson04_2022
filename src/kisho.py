import numpy as np
import os

global ans_num
ans_num = 0
global q_num
q_num = 0

def qna(mondai: str, kotae: str, sentaku: str = None):
    global ans_num
    global q_num
    
    os.system("cls")
    print(mondai)  #問題を表示させる
    
    if sentaku != None: 
        print(f"{i+1} {sentakushi}" for i, sentakushi in enumerate(sentaku))
        ans = input("回答は？: ")
    else: 
        ans = input("回答は？: ")
        
    if ans == kotae:
        print("正解！")
        ans_num += 1
    else:
        print("不正解！")
    
    q_num += 1    
    _ = input()

questions = [
    ["1+1は？", "2", None],
    ["1+1は?", "田んぼの田", None],
    [""]
    ["1+1は?", "田んぼの田", ["2", "1", "3", "田んぼの田"],
    []
]

if __name__ == "__main__":
    
    for i, mondai in enumerate(questions):
        qna(mondai[0], mondai[1], mondai[2])