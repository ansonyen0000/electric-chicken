import os

def Map_Load(_id):
    Map = ""
    p = []
    q = []
    if _id == 0:
        with open(os.getcwd()+os.sep+"Map"+os.sep+"1.txt","rt",encoding="utf-8") as Map1:
            Map = Map1.readlines()
            for i in range(len(Map)):
                print(Map[i],end="")
            print()
    Map_H = len(Map)
    for i in range(Map_H):
        o = Map[i].split("\n")
        Map[i] = o[0]
    Map_W = len(Map[0])
    for i in range(Map_H):
        for j in range(Map_W):
            p += Map[i][j]
        q += p
        p = ""
    return (q,Map_H,Map_W)

def Map_Print(q,Map_H,Map_W,p):
    k = q[p]
    q[p] = "雞"
    for i in range(Map_H):
        o = q[i*Map_H:i*Map_H+Map_W]
        print("".join(o),end="")
        print("")
    q[p] = k

def Player_Move(q,Map_H,Map_W,p,d):
    if d == "w":
        p -= Map_W
        return p
    elif d == "s":
        p += Map_W
        return p
    elif d == "d":
        p += 1
        return p
    elif d == "a":
        p -= 1
        return p
    else:
        return p
