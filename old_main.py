jiei=100
player=100

def status():
  print("-------------")
  print(f"じえいのHP{jiei} 自分のHP{player}")
  print("-------------")

print("じえいとケンカする！")
ans=input("1:殴る 2:煽る 3何もしない")

if ans=='1':
    print('じえいに、「いーかんのっいっかんのっせ～んせいにいちゃうぞ」と言われる。')

    sinario = 1
    print("警察に通報される！")
    sinario = 2

elif ans == "2":
  print("じえいに「〇ね！」と言われる。")

elif ans == "3":
  print("「何もしない」は、選択できません。ご了承ください。")
