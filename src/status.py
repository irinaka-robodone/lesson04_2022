import os
import time

pow = 1
floor = 1
stage = 0
hp = 10

item0 = 0  # item0: 魔法の本 0: 持ってない, 1: 持ってる

def display_stats():
    os.system("cls")
    print("------------------")
    print(f"Stage: {stage}")
    print(f"power: {pow}")
    print(f"floor: {floor}")
    print("------------------")

if __name__ == "__main__":
    
    
    
    display_stats()
    print("test")
    
    ret = input("input current pow :")
    # sp.run(["cls"])
    pow  = int(ret)
    display_stats()
    time.sleep(1)
    pow += 2
    display_stats()