import os,random

def Map_Load(_id):
    Map = ""
    print(_id)
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

def Map_Print(q,Map_H,Map_W,p):
    k = q[p]
    q[p] = "雞"
    for i in range(Map_H):
        o = q[i*Map_W:i*Map_W+Map_W]
        print("".join(o),end="")
        print("")
    q[p] = k
def Player_Move(q,Map_H,Map_W,Chicken,d,t):
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
        if Chicken.Map[0] == 10 and q[o] == "門":
            Chicken.Map[0] = 9
            Chicken.Map[1] = 103
        o = Chicken.Map[1]
