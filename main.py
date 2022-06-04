import os

hpk = 100
hpj = 100

def hyoji(turn, hpk, hpj):
    os.system("cls")
    print("-----------------------")
    print("ターン: ", turn)
    print("かもんHP: ",hpk)
    print("じえいHP: ",hpj)
    print("------------------------")

turn = 1
while not hpk <= 0 and not hpj <= 0:

    hyoji(turn, hpk,hpj)
    print("かもんのターン！")
    sentaku = input("0: パンチ  1: キック    2: 波動拳   3: 熊手打ち　4:頭突き　5:何もしない")

    if sentaku == "0":
        hpj = hpj - 40
    elif sentaku == "1":
        hpk = hpk - 20
    elif sentaku == "2":
        hpj = hpj - 5
    elif sentaku == "3":
        hpj = hpj - 30
    elif sentaku == "4":
        hpj = hpj - 10
    elif sentaku == "5":
        hpj = hpj - 70
    
    hyoji(turn, hpk,hpj)
    if hpj <= 0:
        break

    turn += 1
    hyoji(turn, hpk,hpj)
    print("じえいのターン！")
    sentaku = input("0: パンチ  1: キック    2: 波動拳   3: 熊手打ち　4:頭突き　5:何もしない")

    if sentaku == "0":
        hpj = hpj - 40
    elif sentaku == "1":
        hpk = hpk - 20
    elif sentaku == "2":
        hpj = hpj - 5
    elif sentaku == "3":
        hpj = hpj - 30
    elif sentaku == "4":
        hpj = hpj - 10
    elif sentaku == "5":
        hpj = hpj - 70


hyoji(turn, hpk, hpj)
print("Game Over!")