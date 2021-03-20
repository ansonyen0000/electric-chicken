from Asset import Save,Map,Plot,Chicken_System,Monster_System
import threading,os,time,random

First_Open = 0
#-----------------------------Load()
Day = 0
Time = 0

if os.path.exists(os.getcwd()+os.sep+"save.txt") == True:
    with open(os.getcwd()+os.sep+"save.txt","rt",encoding="utf-8") as save:
        data = save.readlines()
        for i in data:
            a = i.rsplit("\n")
            a = a[0]
            a = exec(a)
if First_Open == 0:
    Day = 0
    Time = 0
    Chicken = Chicken_System.Chicken("棒","瘋狗",0,1,1000,1000,100,100,100,100,10,10,0,[0,55],0)

#-----------------------------Updata()
def Updata():
    while(1):
        time.sleep(0.1)
        p = random.randint(1,10)


updata = threading.Thread(target = Updata, name = 'Updata')
updata.start()

#-----------------------------Save()
def Save_Date(Chicken,p):
    Save.save(Chicken,p,p,p,p)

Save_Date(Chicken,1)
#----------------------------------------------------------Day()
Chicken._EXP(51)
  
while 1:
    re_Monster = 0
    Now_Map = 10
    Mon = []
#-----------------------------Plot()
    if Day == 1:
        Plot.Main_Plot(0)
    if Day == 1:
        Plot.Main_Plot(2)
    if Day == 2:
        Plot.Main_Plot(3)

#-----------------------------Home()
    for i in range(9):
        o = Map.Map_Load(i)
        Mon1 = Monster_System.Mon(i*2)
        Map.Monster_Place(o[0],Mon1)
        Mon2 = Monster_System.Mon(i*2+1)
        Map.Monster_Place(o[0],Mon2)
        Mon.append([Mon1,Mon2])
    while 1:
        if Now_Map == 9 and Chicken.Map[0] == 0:
            for i in range(9):
                o = Map.Map_Load(i)
                Mon1 = Monster_System.Mon(i*2)
                Map.Monster_Place(o[0],Mon1)
                Mon2 = Monster_System.Mon(i*2+1)
                Map.Monster_Place(o[0],Mon2)
                Mon.append([Mon1,Mon2])
        if Chicken.Map[0] >= 9:
            Mon = []
        o = Map.Map_Load(Chicken.Map[0])
        Now_Map = Chicken.Map[0]
        while 1:
            if 0 <= Chicken.Map[0] <= 8:
                Map.Map_Print(o[0],o[1],o[2],Chicken.Map[1],Mon[Chicken.Map[0]])
            else:
                Map.Map_Print(o[0],o[1],o[2],Chicken.Map[1])
            Move = input("")
            if len(Move) == 1:
                Move = Move + "1"
            elif Move[1:].isdigit() == False:
                Move = "w0"
            if 0 <= Chicken.Map[0] <= 8:
                Map.Player_Move(o[0],o[1],o[2],Chicken,Move[:1],int(Move[1:]),Mon[Chicken.Map[0]])
            else:
                Map.Player_Move(o[0],o[1],o[2],Chicken,Move[:1],int(Move[1:]))
            if Now_Map != Chicken.Map[0]:
                break
