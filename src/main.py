import os
import time
import json

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
    
    database = json.load("items.json")
    database.
    
    ret = input("input current pow :")
    # sp.run(["cls"])
    pow  = int(ret)
    display_stats()
    time.sleep(1)
    pow += 2
    display_stats()

    # print("食べる or 飲む を選択肢してください！")
    # kotae = input("1: 食べる or 2: 飲む ")
    
    # while not kotae == "1" or kotae == "2":
    #     kotae = input("1 or 2: ")
    
    # if kotae == "1":
        
    # elif kotae == "2":
        