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

def Map_Print(q,Map_H,Map_W,p,Boss,Chicken,Mon=0):
    k = q[p]
    q[p] = "雞"
    if Mon != 0:
        for i in range(len(Mon)-1):
            if Mon[i].HP > 0:
                q[Mon[i].Map[1]] = "怪"
        if Chicken.Map[0] == 0:
            if Mon[len(Mon)-1].HP > 0 and Boss[0] == 0:
                q[Mon[len(Mon)-1].Map[1]] = "王"
            else:
                q[179] = "\u3000"
                q[199] = "\u3000"
                q[219] = "\u3000"
                q[239] = "\u3000"
        elif Chicken.Map[0] == 1:
            if Mon[len(Mon)-1].HP > 0 and Boss[1] == 0:
                q[Mon[len(Mon)-1].Map[1]] = "王"
            else:
                q[179] = "\u3000"
                q[199] = "\u3000"
                q[219] = "\u3000"
                q[239] = "\u3000"
        elif Chicken.Map[0] == 2:
            if Mon[len(Mon)-1].HP > 0 and Boss[2] == 0:
                q[Mon[len(Mon)-1].Map[1]] = "王"
            else:
                q[388] = "\u3000"
                q[389] = "\u3000"
                q[390] = "\u3000"
                q[391] = "\u3000"
        elif Chicken.Map[0] == 3:
            if Mon[len(Mon)-1].HP > 0 and Boss[3] == 0:
                q[Mon[len(Mon)-1].Map[1]] = "王"
            else:
                q[160] = "\u3000"
                q[180] = "\u3000"
                q[200] = "\u3000"
                q[220] = "\u3000"
        elif Chicken.Map[0] == 4:
            if Mon[len(Mon)-1].HP > 0 and Boss[4] == 0:
                q[Mon[len(Mon)-1].Map[1]] = "王"
            else:
                q[160] = "\u3000"
                q[180] = "\u3000"
                q[200] = "\u3000"
                q[220] = "\u3000"
        elif Chicken.Map[0] == 5:
            if Mon[len(Mon)-1].HP > 0 and Boss[5] == 0:
                q[Mon[len(Mon)-1].Map[1]] = "王"
            else:
                q[388] = "\u3000"
                q[389] = "\u3000"
                q[390] = "\u3000"
                q[391] = "\u3000"
        elif Chicken.Map[0] == 6:
            if Mon[len(Mon)-1].HP > 0 and Boss[6] == 0:
                q[Mon[len(Mon)-1].Map[1]] = "王"
            else:
                q[179] = "\u3000"
                q[199] = "\u3000"
                q[219] = "\u3000"
                q[239] = "\u3000"
        elif Chicken.Map[0] == 7:
            if Mon[len(Mon)-1].HP > 0 and Boss[7] == 0:
                q[Mon[len(Mon)-1].Map[1]] = "王"
            else:
                q[179] = "\u3000"
                q[199] = "\u3000"
                q[219] = "\u3000"
                q[239] = "\u3000"
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
            
def Player_Move(q,Map_H,Map_W,Chicken,d,t,Bag,Mons = 0):
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
                    Mons[j]._State()
                    print('\n是否要對',Mons[j].Name,'進行攻擊 y or n: ',end='')
                    op = input('')
                    if op == "y":
                        a = Attack(Chicken,Mons[j])
                        Chicken._State(0)
                if a == 0:
                    Chicken.HP_ = 0
                if a == 1:
                    Mons.remove(Mons[j])
                    Chicken._MP(-5)
                    q[o] = "\u3000"
                    break
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
        if Chicken.Day >= 6:
            if (Chicken.Map[0] == 9 and (81 <= o and o <=84)):
                Shower(Chicken)
                break
            if (Chicken.Map[0] == 0 and q[o] == "家") or (Chicken.Map[0] == 9 and (86 <= o and o <=89)):
                Chicken.Map[0] = 10
                Chicken.Map[1] = 257
                break
            if (Chicken.Map[0] == 9 and (91 <= o and o <=94)):
                Buy(Bag)
                break
            if (Chicken.Map[0] == 9 and (161 <= o and o <=164)):
                print("你帶著 ",Chicken.Name," 來到了訓練所",end="")
                oo = input("")
                School(Chicken)
                break
            if (Chicken.Map[0] == 9 and (166 <= o and o <=169)):
                Chicken.Map[0] = 0
                Chicken.Map[1] = 190
                break
            if (Chicken.Map[0] == 9 and (171 <= o and o <=174)):
                print("你望著以前工作的地方,心想絕對不要再回到這裡")
                oo = input("")
                break
            if Chicken.Map[0] == 10 and q[o] == "窩":
                break
            if Chicken.Map[0] == 10 and q[o] == "吃":
                Bag.Eat(Chicken)
                break
        else:
            if (Chicken.Map[0] == 9 and (81 <= o and o <=84)):
                print("我不需要去泡溫泉",end='')
                oo = input("")
                break
            if (Chicken.Map[0] == 9 and (86 <= o and o <=89)):
                Chicken.Map[0] = 10
                Chicken.Map[1] = 257
                break
            if (Chicken.Map[0] == 9 and (91 <= o and o <=94)):
                Buy(Bag)
                break
            if (Chicken.Map[0] == 9 and (161 <= o and o <=164)):
                print("我不需要",end='')
                oo = input("")
                break
            if (Chicken.Map[0] == 9 and (166 <= o and o <=169)):
                print("我不需要去探索",end='')
                oo = input("")
                break
            if (Chicken.Map[0] == 9 and (171 <= o and o <=174)):
                Work(Chicken,Bag)
                break
        if Chicken.Map[0] == 10 and q[o] == "門":
            Chicken.Map[0] = 9
            Chicken.Map[1] = 103
            break
        if Chicken.Map[0] == 10 and q[o] == "床":
            Sleep(Chicken)
            break
        o = Chicken.Map[1]
#-----------------------------------戰鬥系統--------------------------------------------
def Attack(Chicken,Mons):
    MyAttack = Chicken.ATK_ - Mons.DF #雞的攻擊
    MonAttack = Mons.ATK - Chicken.DF_ #怪物的攻擊
    if MyAttack <= 0:
        MyAttack = 1
    if MonAttack <= 0:
        MonAttack = 1
    while 1:
        time.sleep(0.5)
        p = random.randint(1,101)
        if p in range(1,10):
            MyFinalAttack = 2*MyAttack
            print('%s 暴擊! 對 %s 造成'%(Chicken.Name,Mons.Name), MyFinalAttack, '點傷害',end="")
        elif p in range(96,100):
            MyFinalAttack = 0
            print('%s 攻擊失誤， %s 成功迴避攻擊'%(Chicken.Name,Mons.Name),end="")
        else:
            MyFinalAttack = MyAttack
            print('%s 對 %s 造成'%(Chicken.Name,Mons.Name), MyFinalAttack, '點傷害',end="")
        print("    ",Chicken.Name,"飽食減少 1")
        Chicken._Hunger(-1)
        Mons._HP(-MyFinalAttack)
        if Mons.HP <= 0:
            time.sleep(0.5)
            print('%s 被 %s 擊殺了'%(Mons.Name,Chicken.Name))
            time.sleep(1)
            print("")
            Chicken._EXP(Mons.EXP)
            return 1
        
        time.sleep(0.5)
        q = random.randint(1,101)
        if q in range(1,10):
            MonFinalAttack = 2*MonAttack
            print('%s 暴擊! 對 %s 造成'%(Mons.Name,Chicken.Name), MonFinalAttack, '點傷害',end="")
        elif q in range(96,100):
            MonFinalAttack = 0
            print('%s 攻擊失誤， %s 成功迴避攻擊'%(Mons.Name,Chicken.Name),end="")
        else:
            MonFinalAttack = MonAttack
            print('%s 對 %s 造成'%(Mons.Name,Chicken.Name), MonFinalAttack, '點傷害',end="")
        print("    ",Chicken.Name,"心情減少 1")
        Chicken._Emotion(-1)
        Chicken._HP(-MonFinalAttack)
        if Chicken.HP_ <= 0:
            time.sleep(0.5)
            print('%s 被 %s 擊殺了'%(Chicken.Name,Mons.Name))
            time.sleep(1)
            print("")
            print('你死了!!')
            return 0

#------------------------------------商店--------------------------------------------
def Buy(Bag):
    Bag.show()
    while True:
        print('--------------------------------------------------------------------------------')
        print('你想買些什麼東西呢 ?')
        print(' 0. 離開商店')
        print(' 1. 有機雞飼料 : 5金幣/袋')
        print('    效果: 行動值增加 1 ,飽食度增加 5')
        print(' 2. 生乳酪蛋糕 : 40金幣/塊')
        print('    效果: 行動值增加 3 ,飽食度增加 15 ,心情增加 15')
        print(' 3. 鴨子造型餅乾 : 80金幣/包')
        print('    效果: 的行動值增加 8 ,飽食度增加 15')
        print(' 4. 特大麥香雞 : 100金幣/個')
        print('    效果: 的行動值增加 20 ,飽食度增加 20')
        print('')
        shop_id = input('請輸入想買的物品編號: ')
        print('')
        if shop_id == "0":
            break
        while 1:
            try:
                num_id = int(input('請輸入購買的個數: '))
                break
            except:
                print("是數字歐~Difficult?")
        print('')
        a=0
        if shop_id == "1" and Bag.Money >= num_id*5:
            Bag.add_money(-1*num_id*5)
            Bag.add_food( (num_id) * 1)
            print('獲得了 ',num_id,' 個有機雞飼料 ! ! ')                
            time.sleep(0.5)
            a=1
            print('--------------------------------------------------------------------------------')
            Bag.show()            
        elif shop_id == "2" and Bag.Money >= num_id*40:
            Bag.add_money(-1*num_id*40)
            Bag.add_cake(num_id)
            print('獲得了 ',num_id,' 個生乳酪蛋糕 ! ! ')
            time.sleep(0.5)
            a=1
            print('--------------------------------------------------------------------------------')
            Bag.show()
        elif shop_id == "3" and Bag.Money >= num_id*80:
            Bag.add_money(-1*num_id*80)
            Bag.add_cookies(num_id)
            print('獲得了 ',num_id,' 個鴨子造型餅乾 ! ! ')
            time.sleep(0.5)
            a=1
            print('--------------------------------------------------------------------------------')
            Bag.show()
        elif shop_id == "4" and Bag.Money >= num_id*100:
            Bag.add_money(-1*num_id*100)
            Bag.add_hamburger(num_id)
            print('獲得了 ',num_id,' 個特大麥香雞 ! ! ')
            time.sleep(0.5)
            a=1
            print('--------------------------------------------------------------------------------')
            Bag.show()                    
        if a!=1:
            print("口袋空空,錢不夠握~~~",end="")
            oo = input("")
            print('--------------------------------------------------------------------------------')
            Bag.show()
#------------------------------------工作--------------------------------------------
def Work(Chichen,Bag):
    print("八小時候....")
    time.sleep(1)
    print("你賺了200元")
    time.sleep(1)
    Chicken.Add_Time(240)
    Bag.add_money(200)
    
#------------------------------------澡堂--------------------------------------------
def Shower(Chicken):
    print("你決定帶著",Chicken.Name,"來泡溫泉")
    time.sleep(1)
    print("三小時候.....")
    time.sleep(1)
    Chicken.Add_Time(90)
    Chicken._HP(Chicken.HP/2)
    Chicken._Hunger(-5)
    Chicken._MP(Chicken.MP)
    print("行動值增加 20 ,飽食度減少 5 ,心情增加 10")
    time.sleep(1)
#------------------------------------點數--------------------------------------------
def School(Chicken):
    while 1:
        if Chicken.Point > 0:
            Chicken._State(1)
            print("目前的點數為: ",Chicken.Point)
            print("0.退出")
            print("1.血量最大值加10")
            print("2.攻擊加3")
            print("3.防禦加3\n")
            c = input("請選擇你要的升級:")
            if c == "0":
                break
            if c == "1":
                Chicken.HP += 10
                print(Chicken.HP)
                Chicken._HP(10)
                Chicken.Point -= 1
            elif c == "2":
                Chicken.ATK += 3
                Chicken._ATK(3)
                Chicken.Point -= 1
            elif c == "3":
                Chicken.DF += 3
                Chicken._DF(13)
                Chicken.Point -= 1
        else:
            print("\n點數不足\m")
            break
#------------------------------------睡覺--------------------------------------------
def Sleep(Chicken):
    print("睡個了好覺!",end = "")
    oo = input("")
    Chicken.Time = 210
    Chicken.Day += 1
    Chicken._Hunger(-10)
    Chicken._Emotion(+50)
    Chicken._HP(Chicken.HP)
    Chicken._MP(Chicken.MP)
