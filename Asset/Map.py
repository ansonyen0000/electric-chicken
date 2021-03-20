import os,random,math,time

def Map_Load(_id):
    Map = ""
    p = []
    q = []
    if _id == 0: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"0.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 1: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"1.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 2: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"2.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 3: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"3.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 4: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"4.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 5: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"5.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 6: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"6.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 7: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"7.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 8: #野外
        with open(os.getcwd()+os.sep+"Map"+os.sep+"8.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 9: #主頁面
        with open(os.getcwd()+os.sep+"Map"+os.sep+"主頁面地圖.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    if _id == 10: #主頁面
        with open(os.getcwd()+os.sep+"Map"+os.sep+"房間.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
    Map_H = len(Map)
    for i in range(Map_H):
        o = Map[i].split("\n")
        Map[i] = o[0]
    Map_W = len(Map[0])
    for i in range(Map_H):
        for j in range(Map_W):
            p += Map[i][j]
    return (p,Map_H,Map_W)

def Map_Print(q,Map_H,Map_W,p,Mon=0):
    k = q[p]
    q[p] = "雞"
    if Mon != 0:
        for i in range(len(Mon)):
            if Mon[i].HP > 0:
                q[Mon[i].Map[1]] = "怪"
    H  = int(p/Map_W)+1
    W = p%Map_W+1
    ppo = ""
    print("")
    for i in range(Map_H):
        ppo = abs(i+1-H)
        if ppo == 1:
            s = "一"
        elif ppo == 2:
            s = "二"
        elif ppo == 3:
            s = "三"
        elif ppo == 4:
            s = "四"
        elif ppo == 5:
            s = "五"
        elif ppo == 6:
            s = "六"
        elif ppo == 7:
            s = "七"
        elif ppo == 8:
            s = "八"
        elif ppo == 9:
            s = "九"
        else:
            s = ""
        o = q[i*Map_W:i*Map_W+Map_W]
        print("".join(o),s,end="",sep="\u3000")
        print("")
    print("")
    for i in range(Map_W):
        ppo = abs(i+1-W)
        if ppo == 1:
            print("一",end = "")
        elif ppo == 2:
            print("二",end = "")
        elif ppo == 3:
            print("三",end = "")
        elif ppo == 4:
            print("四",end = "")
        elif ppo == 5:
            print("五",end = "")
        elif ppo == 6:
            print("六",end = "")
        elif ppo == 7:
            print("七",end = "")
        elif ppo == 8:
            print("八",end = "")
        elif ppo == 9:
            print("九",end = "")
        else:
            print("\u3000",end = "")
    print("")
    q[p] = k
    
def Monster_Place(q,Mon):
    while 1:
        p = random.randint(0,len(q)-1)
        if q[p] == "\u3000":
            Mon.Map = [Mon.Map[0],p]
            break
            
def Player_Move(q,Map_H,Map_W,Chicken,d,t,Mons = 0):
    o = Chicken.Map[1]
    for i in range(t):
        if d == "w":
            o -= Map_W
            if q[o] == "\u3000":
                Chicken.Map[1] = o
        elif d == "s":
            o += Map_W
            if q[o] == "\u3000":
                Chicken.Map[1] = o
        elif d == "d":
            o += 1
            if q[o] == "\u3000":
                Chicken.Map[1] = o
        elif d == "a":
            o -= 1
            if q[o] == "\u3000":
                Chicken.Map[1] = o
        a = 2
        if Mons != 0:
            for j in range(len(Mons)):
                if Mons[j].Map[1] == o and Mons[j].HP > 0:
                    a = Attack(Chicken,Mons[j])
                if a == 0:
                    pe = 1
                    break
                if a == 1:
                    Mons.remove(Mons[j])
                    q[o] = "\u3000"
                    return Mons
        if Chicken.Map[1]%Map_W == 19:
            Chicken.Map[0] += 1
            Chicken.Map[1] -= Map_W-1
            break
        if Chicken.Map[1]%Map_W == 0:
            Chicken.Map[0] -= 1
            Chicken.Map[1] += Map_W-1
            break
        if Chicken.Map[1]/Map_W < 1:
            Chicken.Map[0] -= 3
            Chicken.Map[1] += (Map_H-1)*(Map_W)
            break
        if (Chicken.Map[1])/Map_W >= Map_H-1:
            Chicken.Map[0] += 3
            Chicken.Map[1] -= (Map_H-1)*(Map_W)
            break
        if (Chicken.Map[0] == 0 and q[o] == "家") or (Chicken.Map[0] == 9 and (86 <= o and o <=89)):
            Chicken.Map[0] = 10
            Chicken.Map[1] = 257
            break
        if (Chicken.Map[0] == 9 and (166 <= o and o <=169)):
            Chicken.Map[0] = 0
            Chicken.Map[1] = 190
            break
        if Chicken.Map[0] == 10 and q[o] == "門":
            Chicken.Map[0] = 9
            Chicken.Map[1] = 103
            break
        o = Chicken.Map[1]
        
def Attack(Chicken,Mons):
    MyAttack = Chicken.ATK - Mons.DF #雞的攻擊
    MonAttack = Mons.ATK - Chicken.DF #怪物的攻擊
    if MyAttack <= 0:
        MyAttack = 1
    if MonAttack <= 0:
        MonAttack = 1
    while 1:
        time.sleep(0.5)
        p = random.randint(1,101)
        if p in range(1,10):
            MyFinalAttack = 2*MyAttack
            print('%s 暴擊! 對 %s 造成'%(Chicken.Name,Mons.Name), MyFinalAttack, '點傷害')
        elif p in range(96,100):
            MyFinalAttack = 0
            print('%s 攻擊失誤， %s 成功迴避攻擊'%(Chicken.Name,Mons.Name))
        else:
            MyFinalAttack = MyAttack
            print('%s 對 %s 造成'%(Chicken.Name,Mons.Name), MyFinalAttack, '點傷害')
        Mons._HP(-MyFinalAttack)
        if Mons.HP <= 0:
            time.sleep(0.5)
            print('%s 被 %s 擊殺了'%(Mons.Name,Chicken.Name))
            return 1
            break
        
        time.sleep(0.5)
        q = random.randint(1,101)
        if q in range(1,10):
            MonFinalAttack = 2*MonAttack
            print('%s 暴擊! 對 %s 造成'%(Mons.Name,Chicken.Name), MonFinalAttack, '點傷害')
        elif q in range(96,100):
            MonFinalAttack = 0
            print('%s 攻擊失誤， %s 成功迴避攻擊'%(Mons.Name,Chicken.Name))
        else:
            MonFinalAttack = MonAttack
            print('%s 對 %s 造成'%(Mons.Name,Chicken.Name), MonFinalAttack, '點傷害')
            
            Chicken._HP(-MonFinalAttack)
        if Chicken._HP <= 0:
            time.sleep(0.5)
            print('%s 被 %s 擊殺了'%(Chicken.Name,Mons.Name))
            print('你死了!!')
            return 0
            break
