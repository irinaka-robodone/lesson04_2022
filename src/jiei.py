import numpy as np

def main():
    
    print("なに！敵が現れた！！")
    _ = input()
    random = np.random.rand() # 0~1のランダムな数をつくって random に代入
    if random < 1/3:
        print("回避！")
    else: 
        print("ｳｹﾞｯ...攻撃を食らってしまった...")
        
        
if __name__ == "__main__":
    main()