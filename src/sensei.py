import os
import time
import json

item0 = 0  # item0: 魔法の本 0: 持ってない, 1: 持ってる

stats = {"power": 10, "hp": 10, "mp": 10, "speed": 10}
data = {"floor": 0, "company": 0}

def display_stats():
    os.system("cls")
    print("------------------")
    for key, value in stats.items():
        print(f"{key}: {value}")
    for key, value in data.items():
        if value != 0:
            print(f"{key}: {value}")
    print("------------------")
    
def is_game_over(hp):
    if hp < 0:
        return True
    else: return False

def make_senario(id, messages_early: list, choices: dict = None, messages_later: list = None):
    
    os.system("cls")
    display_stats()
    print(f"senario id: {id}")
    
    if type(messages_early) == list:
        for mes in messages_early:
            print(f"{mes}")
    else: 
        print(f"{messages_early}")
    
    i = 0
    for choice in choices.values():
        print(f"{i}: {choice}", end="   ")
        i += 1
    is_ok_choice = False
    print("")
    while not is_ok_choice:
        usr_choice = input()
        try: 
            # usr_choice = int(usr_choice)
            glob_choice = list(choices.keys())[int(usr_choice)]
            print(f"なるほど、「{choices[glob_choice]}」を選ぶのだな。よかろう。")
            is_ok_choice = True
        except:
            i = 0
            for choice in choices.values():
                print(f"{i}: {choice}", end="   ")
                i += 1
            print("(半角の数字で選択してください)")
    
    if messages_later is None:
        _ = input()
        return glob_choice, is_game_over(stats["hp"])
    elif type(messages_later) == list:
        for mes in messages_later:
            print(f"{mes}")
    else: 
        print(f"{messages_later}")
    
    _ = input()
    return glob_choice, is_game_over(stats["hp"])
    

if __name__ == "__main__":
    
    gameover = False
    glob_choice = 0
    
    with open('senario.json', errors="ignore", encoding="utf-8") as f:
            senarios = json.load(f)
    
    while not gameover: 
        
        senario = senarios[f"{glob_choice}"]
        glob_choice, gameover = make_senario(glob_choice, senario["mes_e"], senario["choice"])
        
        print(f"senario: {glob_choice}, GameOver?: {gameover}")