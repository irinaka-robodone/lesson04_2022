import os
import numpy as np
yuki = 5
pawa = 5
HP = 30
item1 = 0 # item1: 魔法の本

def meta(kekka=""):
    os.system("cls")
    print("--------------------------")
    print(f"yuki {yuki} pawa {pawa} HP {HP}" )
    print(kekka)
    print("--------------------------")
    
    
def yoke(kakuritu):
    yokeru = np.random.rand()
    if yokeru < kakuritu:
        return True
    else:
        return False
    
    
meta()
print("ダンジョンに入る")
_ = input()
os.system("cls")
print("敵が現れた！")
_ = input()
os.system("cls")
inp = input("1:逃げる？ or 2:戦う？:")

while inp != "1" and inp != "2":
    inp = input("1:逃げる？ or 2:戦う？:")
if inp == "1":
    yuki = yuki - 2
    meta()
    print("勇気が2下がった")
    _ = input()
elif inp == "2":
    yuki = yuki + 3
    pawa = pawa + 2
    meta()
    print("敵を倒した 勇気が３上がった 力が2上がった")
    _ = input()
print("分かれ道だ！")
_ = input()
inp = input("1:左に行く? or 2:右に行く?:")
if inp == "1":
    print("上質な魔法の本を手に入れた")
    print(" 避けるを習得した 敵の攻撃によって避けられる確率が変わる")
    _ = input()
    item1 = 1
elif inp == "2":
    pawa += 3
    meta()
    print("ご飯があった！ 食べた 力が3がった")
    _ = input()
if item1 == 1:
    print("ゴブリンの攻撃")
    _ = input()
    kaihi = yoke(1/3)
    
    if kaihi == False:
        print("当たってしまった")
        HP -= 9
    elif kaihi ==  True:
        print("回避できた")
        _ = input()